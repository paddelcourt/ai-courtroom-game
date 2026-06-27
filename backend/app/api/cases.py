from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from app.api.deps import get_db
from app.services.case_generation_service import generate_and_store_case
from app.services.case_service import get_case, list_cases
from app.services.evidence_service import get_evidence, list_evidence
from app.services.testimony_service import get_testimony, list_testimony
from app.services.character_service import get_character, list_character
from app.models.case import Case
from app.schemas.case import CaseRead
from app.schemas.evidence import EvidenceRead
from app.schemas.character import CharacterRead
from app.schemas.testimony import TestimonyStatementRead
from app.schemas.defense_choice import DefenseChoiceRead

router = APIRouter()


@router.post("/generate", response_model=CaseRead)
def generate_case(db: Session = Depends(get_db), theme: str = "museum theft") -> Case:

    result = generate_and_store_case(db, theme)
    if not result:
        raise HTTPException(status_code=400, detail="request failed")
    return result


@router.get("/{case_id}", response_model=CaseRead)
def read_case(db: Session = Depends(get_db), case_id: str = ""):
    result = get_case(db, case_id)
    if not result:
        raise HTTPException(status_code=404, detail="could not find case")
    return result

    
@router.get("", response_model=List[CaseRead])
def read_all_case(db: Session = Depends(get_db)):
    result = list_cases(db)
    if not result:
        raise HTTPException(status_code=404, detail="could not find any case")
    return result

@router.get("/{case_id}/evidence", response_model=list[EvidenceRead])
def read_evidence(db: Session = Depends(get_db), case_id: str = ""):
    result = list_evidence(db, case_id)
    if not result:
        raise HTTPException(status_code=404, detail="could not find evidence")
    return result

@router.get("/{case_id}/testimony", response_model=list[TestimonyStatementRead])
def read_testimony(db: Session = Depends(get_db), case_id: str = ""):
    result = list_testimony(db, case_id)
    if not result:
        raise HTTPException(status_code=404, detail="could not find testimony")
    return result

@router.get("/{case_id}/characters", response_model=list[CharacterRead])
def read_case_characters(
    case_id: str,
    db: Session = Depends(get_db),
):
    result = list_character(db, case_id)
    if not result:
        raise HTTPException(status_code=404, detail="could not find characters")
    return result