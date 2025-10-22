# app/routers/guides.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import BuildGuide, Character
from ..schemas.build_guide import BuildGuideResponse

router = APIRouter(prefix="/api/guides", tags=["build_guides"])

@router.get("/", response_model=List[BuildGuideResponse])
def get_all_build_guides(db: Session = Depends(get_db)):
    guides = db.query(BuildGuide).all()
    response = []

    for g in guides:
        response.append(
            BuildGuideResponse(
                id=g.id,
                character_id=g.character_id,
                character_name=g.character.name if g.character else "Unknown",
                title=g.title,
                description=g.description,
                picture_path=g.picture_path,
                created_at=g.created_at.isoformat(),  # convert datetime -> string
                uploads=[{"id": u.id, "image_path": u.image_path, "caption": u.caption, "uploaded_at": u.uploaded_at.isoformat()} for u in g.uploads]
            )
        )
    return response

@router.get("/{guide_id}", response_model=BuildGuideResponse)
def get_build_guide(guide_id: int, db: Session = Depends(get_db)):
    guide = db.query(BuildGuide).filter(BuildGuide.id == guide_id).first()
    if not guide:
        raise HTTPException(status_code=404, detail="Guide not found")
    character = db.query(Character).filter(Character.id == guide.character_id).first()
    return BuildGuideResponse(
        id=guide.id,
        character_id=guide.character_id,
        title=guide.title,
        description=guide.description,
        created_at=guide.created_at,
        picture_path=guide.picture_path,
        character=character
    )
