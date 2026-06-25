from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.case import CaseCreate, CaseRead
from app.services.case_service import create_case, get_case, list_cases

router = APIRouter()


@router.get("", response_model=list[CaseRead])
def read_cases(db: Session = Depends(get_db)) -> list[CaseRead]:
    return list_cases(db)


@router.post("", response_model=CaseRead, status_code=status.HTTP_201_CREATED)
def create_new_case(payload: CaseCreate, db: Session = Depends(get_db)) -> CaseRead:
    return create_case(db, payload)


@router.get("/{case_id}", response_model=CaseRead)
def read_case(case_id: int, db: Session = Depends(get_db)) -> CaseRead:
    case = get_case(db, case_id)
    if case is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")
    return case
