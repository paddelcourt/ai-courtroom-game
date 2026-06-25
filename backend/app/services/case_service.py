from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.case import Case
from app.schemas.case import CaseCreate


def list_cases(db: Session) -> list[Case]:
    return list(db.scalars(select(Case).order_by(Case.id.desc())))


def get_case(db: Session, case_id: int) -> Case | None:
    return db.get(Case, case_id)


def create_case(db: Session, payload: CaseCreate) -> Case:
    case = Case(title=payload.title, description=payload.description)
    db.add(case)
    db.commit()
    db.refresh(case)
    return case
