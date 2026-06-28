from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from app.services.character_service import get_character

from app.api.deps import get_db
from app.schemas.character import CharacterRead


router = APIRouter()


@router.get("/{character_id}", response_model=CharacterRead)
def read_character(db: Session = Depends(get_db), character_id: str = ""):
    result = get_character(db, character_id)
    if not result:
        raise HTTPException(status_code=404, detail="could not find testimony")
    return result

