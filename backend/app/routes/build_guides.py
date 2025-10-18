from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List
import os
import shutil
from datetime import datetime
from ..database import get_db
from ..models import BuildGuide, Upload
from ..schemas.build_guide import BuildGuideCreate, BuildGuideResponse, UploadCreate
from ..middleware.auth import verify_token
from ..config import settings

router = APIRouter(prefix="/api/guides", tags=["build_guides"])


@router.post("/", response_model=BuildGuideResponse)
async def create_guide(
        guide: BuildGuideCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(verify_token)
):
    new_guide = BuildGuide(**guide.dict())
    db.add(new_guide)
    db.commit()
    db.refresh(new_guide)
    return new_guide


@router.get("/", response_model=List[BuildGuideResponse])
async def get_all_guides(db: Session = Depends(get_db)):
    guides = db.query(BuildGuide).all()
    return guides


@router.get("/{guide_id}", response_model=BuildGuideResponse)
async def get_guide(guide_id: int, db: Session = Depends(get_db)):
    guide = db.query(BuildGuide).filter(BuildGuide.id == guide_id).first()
    if not guide:
        raise HTTPException(status_code=404, detail="Guide not found")
    return guide


@router.post("/{guide_id}/upload")
async def upload_image(
        guide_id: int,
        file: UploadFile = File(...),
        caption: str = Form(..., min_length=5, max_length=200),
        db: Session = Depends(get_db),
        current_user: dict = Depends(verify_token)
):
    # Validate guide exists
    guide = db.query(BuildGuide).filter(BuildGuide.id == guide_id).first()
    if not guide:
        raise HTTPException(status_code=404, detail="Guide not found")

    # Validate file type
    file_ext = file.filename.split(".")[-1].lower()
    if file_ext not in settings.ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # Validate file size
    file.file.seek(0, 2)  # Seek to end
    file_size = file.file.tell()
    file.file.seek(0)  # Reset to beginning

    if file_size > settings.MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large (max 2MB)")

    # Save file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    file_path = os.path.join(settings.UPLOAD_DIR, filename)

    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Save to database
        upload = Upload(
            build_guide_id=guide_id,
            image_path=file_path,
            caption=caption
        )
        db.add(upload)
        db.commit()
        db.refresh(upload)

        return upload

    except Exception as e:
        # Delete file if database save fails
        if os.path.exists(file_path):
            os.remove(file_path)
        raise HTTPException(status_code=500, detail=str(e))