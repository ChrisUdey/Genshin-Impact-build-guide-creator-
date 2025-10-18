from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import Character

router = APIRouter(prefix="/api/characters", tags=["characters"])

@router.get("/")
async def get_all_characters(db: Session = Depends(get_db)):
    characters = db.query(Character).all()
    return characters

@router.get("/{character_id}")
async def get_character(character_id: int, db: Session = Depends(get_db)):
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character