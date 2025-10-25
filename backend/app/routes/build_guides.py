# app/routers/guides.py
import datetime
import os

from fastapi import APIRouter, Depends, HTTPException, Form, File, UploadFile
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import BuildGuide, Character
from ..schemas.build_guide import BuildGuideResponse

router = APIRouter(prefix="/api/guides", tags=["build_guides"])


@router.get("/pending", response_model=List[BuildGuideResponse])
def get_pending_guides(db: Session = Depends(get_db)):
    guides = db.query(BuildGuide).filter(BuildGuide.status == "pending").all()
    response = []
    for g in guides:
        response.append(
            BuildGuideResponse(
                id=g.id,
                username=g.username,
                character_id=g.character_id,
                character_name=g.character.name if g.character else "Unknown",
                title=g.title,
                description=g.description,
                picture_path=g.picture_path,
                created_at=g.created_at.isoformat(),
                uploads=[{"id": u.id, "image_path": u.image_path, "caption": u.caption, "uploaded_at": u.uploaded_at.isoformat()} for u in g.uploads]
            )
        )
    return response


@router.patch("/{guide_id}/approve")
def approve_guide(guide_id: int, db: Session = Depends(get_db)):
    guide = db.query(BuildGuide).filter(BuildGuide.id == guide_id).first()
    if not guide:
        raise HTTPException(status_code=404, detail="Guide not found")
    guide.status = "approved"
    db.commit()
    return {"detail": "Guide approved"}

@router.delete("/{guide_id}")
def reject_guide(guide_id: int, db: Session = Depends(get_db)):
    guide = db.query(BuildGuide).filter(BuildGuide.id == guide_id).first()
    if not guide:
        raise HTTPException(status_code=404, detail="Guide not found")
    db.delete(guide)
    db.commit()
    return {"detail": "Guide rejected"}

@router.get("/", response_model=List[BuildGuideResponse])
def get_all_build_guides(db: Session = Depends(get_db)):
    guides = db.query(BuildGuide).filter(BuildGuide.status == "approved").all()
    response = []

    for g in guides:
        response.append(
            BuildGuideResponse(
                id=g.id,
                username=g.username,
                character_id=g.character_id,
                character_name=g.character.name if g.character else "Unknown",
                title=g.title,
                description=g.description,
                picture_path=g.picture_path,
                created_at=g.created_at.isoformat(),
                status=g.status,
                uploads=[
                    {
                        "id": u.id,
                        "image_path": u.image_path,
                        "caption": u.caption,
                        "uploaded_at": u.uploaded_at.isoformat()
                    }
                    for u in g.uploads
                ],
            )
        )
    return response



# GET a specific guide (any status)
@router.get("/{guide_id}", response_model=BuildGuideResponse)
def get_build_guide(guide_id: int, db: Session = Depends(get_db)):
    guide = db.query(BuildGuide).filter(BuildGuide.id == guide_id).first()
    if not guide:
        raise HTTPException(status_code=404, detail="Guide not found")
    character = db.query(Character).filter(Character.id == guide.character_id).first()
    return BuildGuideResponse(
        id=guide.id,
        username=guide.username,
        character_id=guide.character_id,
        character_name=character.name if character else "Unknown",
        title=guide.title,
        description=guide.description,
        picture_path=guide.picture_path,
        created_at=guide.created_at.isoformat(),
        status=guide.status,
        uploads=[],
    )


# PUT approve a guide (admin use)
@router.put("/{guide_id}/approve")
def approve_build_guide(guide_id: int, db: Session = Depends(get_db)):
    guide = db.query(BuildGuide).filter(BuildGuide.id == guide_id).first()
    if not guide:
        raise HTTPException(status_code=404, detail="Guide not found")

    guide.status = "approved"
    db.commit()
    db.refresh(guide)
    return {"message": f"Guide {guide_id} approved successfully"}


UPLOAD_DIR = os.path.join("app", "static", "build_pics")
os.makedirs(UPLOAD_DIR, exist_ok=True)



@router.post("/", response_model=BuildGuideResponse)
def create_build_guide(
    username: str = Form(...),
    character_name: str = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    picture: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    # find character
    character = db.query(Character).filter(Character.name == character_name).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    picture_path = None
    if picture:
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}_{picture.filename}"
        save_path = os.path.join("app/static/build_pics", filename)
        with open(save_path, "wb") as f:
            f.write(picture.file.read())
        picture_path = f"build_pics/{filename}"

    guide = BuildGuide(
        username=username,
        character_id=character.id,
        title=title,
        description=description,
        picture_path=picture_path,
        status="pending",  # 🆕 automatically pending
    )

    db.add(guide)
    db.commit()
    db.refresh(guide)

    return BuildGuideResponse(
        id=guide.id,
        username=guide.username,
        character_id=guide.character_id,
        character_name=character.name,
        title=guide.title,
        description=guide.description,
        picture_path=guide.picture_path,
        created_at=guide.created_at.isoformat(),
        status=guide.status,
        uploads=[],
    )