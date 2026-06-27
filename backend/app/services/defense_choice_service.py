from sqlmodel import Session, select

from app.models.defense_choice import DefenseChoice
from app.schemas.defense_choice import DefenseChoiceCreate


def create_defense_choice(db: Session, payload: DefenseChoiceCreate) -> DefenseChoice:
    defense_choice = DefenseChoice(
        testimony_statement_id=payload.testimony_statement_id,
        text=payload.text,
        is_correct=payload.is_correct,
        feedback=payload.feedback,
        prosecutor_response=payload.prosecutor_response,
        judge_response=payload.judge_response,
    )

    db.add(defense_choice)
    db.commit()
    db.refresh(defense_choice)

    return defense_choice

def list_defense_choice(db: Session, testimony_statement_id: str) -> list[DefenseChoice]:
    return list(db.exec(select(DefenseChoice).where(DefenseChoice.testimony_statement_id == testimony_statement_id)).all())


def get_defense_choice(db: Session, defense_id: str) -> DefenseChoice | None:
    return db.get(DefenseChoice, defense_id)
