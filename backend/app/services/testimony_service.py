from sqlmodel import Session, select

from app.models.testimony import TestimonyStatement
from app.schemas.testimony import TestimonyStatementCreate, TestimonyStatementRead


def create_testimony(db: Session, payload: TestimonyStatementCreate) -> TestimonyStatement:
    testimony_statement = TestimonyStatement(
        case_id=payload.case_id,
        character_id=payload.character_id,
        text=payload.text,
        order_index=payload.order_index
    )

    db.add(testimony_statement)
    db.commit()
    db.refresh(testimony_statement)

    return testimony_statement

def list_testimony(db: Session, case_id: str) -> list[TestimonyStatement]:
    statement = (
    select(TestimonyStatement)
    .where(TestimonyStatement.case_id == case_id)
    .order_by(TestimonyStatement.order_index)
)
    return list(db.exec(statement).all())


def get_testimony(db: Session, testimony_id: str) -> TestimonyStatement | None:
    return db.get(TestimonyStatement, testimony_id)