# app/routes/build_guides.py

import os
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Form, File, UploadFile, status
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import ValidationError
from ..database import get_db
from ..models import BuildGuide, Character
from ..schemas.build_guide import BuildGuideResponse, BuildGuideFormCreate

router = APIRouter(prefix="/api/guides", tags=["build_guides"])


@router.get("/pending", response_model=List[BuildGuideResponse])
def get_pending_guides(db: Session = Depends(get_db)):
    """Get all pending guides awaiting approval"""
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
                status=g.status,
                uploads=[
                    {
                        "id": u.id,
                        "image_path": u.image_path,
                        "caption": u.caption,
                        "uploaded_at": u.uploaded_at.isoformat()
                    }
                    for u in g.uploads
                ]
            )
        )
    return response


@router.patch("/{guide_id}/approve")
def approve_guide(guide_id: int, db: Session = Depends(get_db)):
    """Approve a pending guide"""
    guide = db.query(BuildGuide).filter(BuildGuide.id == guide_id).first()
    if not guide:
        raise HTTPException(status_code=404, detail="Guide not found")
    guide.status = "approved"
    db.commit()
    return {"detail": "Guide approved"}


@router.delete("/{guide_id}")
def reject_guide(guide_id: int, db: Session = Depends(get_db)):
    """Reject and delete a guide"""
    guide = db.query(BuildGuide).filter(BuildGuide.id == guide_id).first()
    if not guide:
        raise HTTPException(status_code=404, detail="Guide not found")
    db.delete(guide)
    db.commit()
    return {"detail": "Guide rejected"}


@router.get("/", response_model=List[BuildGuideResponse])
def get_all_build_guides(db: Session = Depends(get_db)):
    """Get all approved build guides"""
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


@router.get("/{guide_id}", response_model=BuildGuideResponse)
def get_build_guide(guide_id: int, db: Session = Depends(get_db)):
    """Get a specific guide by ID"""
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


@router.put("/{guide_id}/approve")
def approve_build_guide(guide_id: int, db: Session = Depends(get_db)):
    """Approve a guide (admin use)"""
    guide = db.query(BuildGuide).filter(BuildGuide.id == guide_id).first()
    if not guide:
        raise HTTPException(status_code=404, detail="Guide not found")

    guide.status = "approved"
    db.commit()
    db.refresh(guide)
    return {"message": f"Guide {guide_id} approved successfully"}


UPLOAD_DIR = os.path.join("app", "static", "build_pics")
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/", response_model=BuildGuideResponse, status_code=status.HTTP_201_CREATED)
def create_build_guide(
        username: str = Form(...),
        character_name: str = Form(...),
        title: str = Form(...),
        description: str = Form(...),
        picture: Optional[UploadFile] = File(None),
        db: Session = Depends(get_db)
):
    """


    Validates:
    - Username: 4-20 chars, alphanumeric
    - Title: 4-30 chars
    - Description: 10-350 chars
    - Character: Must exist in database
    - Picture: JPG/PNG only, max 2MB, no WebP
    """


    try:
        validated_data = BuildGuideFormCreate(
            username=username,
            character_name=character_name,
            title=title,
            description=description
        )
    except ValidationError as e:
        # Extract validation errors into readable format
        errors = {}
        for error in e.errors():
            field = error['loc'][0]
            message = error['msg']
            errors[field] = message

        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "validation_errors": errors,
                "message": "Invalid input data. Please check the errors above."
            }
        )


    character = db.query(Character).filter(
        Character.name == validated_data.character_name
    ).first()

    if not character:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Character '{validated_data.character_name}' not found in database"
        )


    picture_path = None
    if picture:
        # Check content type
        allowed_types = ['image/jpeg', 'image/jpg', 'image/png']
        if picture.content_type not in allowed_types:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only JPG, JPEG, and PNG images are allowed. WebP is not supported."
            )

        # Check for WebP by filename
        if picture.filename and picture.filename.lower().endswith('.webp'):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="WebP images are not supported. Please upload JPG or PNG."
            )

        # Read and validate file size
        try:
            contents = picture.file.read()
            file_size = len(contents)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Failed to read uploaded file: {str(e)}"
            )

        # Check file size (2MB max)
        max_size = 2 * 1024 * 1024  # 2MB in bytes
        if file_size > max_size:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"File size ({file_size / 1024 / 1024:.2f}MB) exceeds maximum allowed size (2MB)"
            )

        # Check file isn't empty
        if file_size == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Uploaded file is empty"
            )

        # Save file with safe filename
        timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        safe_filename = picture.filename.replace(" ", "_") if picture.filename else "upload.jpg"
        filename = f"{timestamp}_{safe_filename}"
        save_path = os.path.join("app/static/build_pics", filename)

        try:
            with open(save_path, "wb") as f:
                f.write(contents)
            picture_path = f"build_pics/{filename}"
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to save file to server: {str(e)}"
            )


    guide = BuildGuide(
        username=validated_data.username,
        character_id=character.id,
        title=validated_data.title,
        description=validated_data.description,
        picture_path=picture_path,
        status="pending",
    )

    try:
        db.add(guide)
        db.commit()
        db.refresh(guide)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create guide in database: {str(e)}"
        )


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