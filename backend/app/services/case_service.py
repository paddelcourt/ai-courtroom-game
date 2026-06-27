from sqlmodel import Session, select

from app.models.case import Case
from app.schemas.case import CaseCreate


def list_cases(db: Session) -> list[Case]:
    return list(db.exec(select(Case).order_by(Case.title)).all())


def get_case(db: Session, case_id: str) -> Case | None:
    return db.get(Case, case_id)


def create_case(db: Session, payload: CaseCreate) -> Case:
    case = Case(
        title=payload.title,
        description=payload.description,
    )

    db.add(case)
    db.commit()
    db.refresh(case)

    return case
