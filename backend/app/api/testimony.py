from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from app.api.deps import get_db
from app.services.testimony_service import get_testimony, list_testimony
from app.services.defense_choice_service import get_defense_choice, list_defense_choice
from app.schemas.testimony import TestimonyStatementRead
from app.schemas.defense_choice import DefenseChoiceRead


router = APIRouter()


@router.get("/{testimony_id}/choices", response_model=list[DefenseChoiceRead])
def read_testimony(db: Session = Depends(get_db), testimony_id: str = ""):
    result = list_defense_choice(db, testimony_id)
    if not result:
        raise HTTPException(status_code=404, detail="could not find testimony")
    return result

