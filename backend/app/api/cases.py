from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.api.deps import get_db
from app.services.case_generation_service import generate_and_store_case
from app.models.case import Case
from app.schemas.case import CaseRead

router = APIRouter()


@router.post("/generate", response_model=CaseRead)
def generate_case(db: Session = Depends(get_db), theme: str = "museum theft") -> Case:

    result = generate_and_store_case(db, theme)
    if not result:
        raise HTTPException(status_code=400, detail="request failed")
    return result


@router.get("/generate", response_model=CaseRead)
def get_