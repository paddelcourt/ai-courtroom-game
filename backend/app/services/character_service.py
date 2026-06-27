from sqlmodel import Session, select

from app.models.character import Character
from app.schemas.character import CharacterCreate, CharacterBase, CharacterRead


def create_character(db: Session, payload: CharacterCreate) -> Character:
    character = Character(
        case_id=payload.case_id,
        name=payload.name,
        description=payload.description,
        role=payload.role,
)

    db.add(character)
    db.commit()
    db.refresh(character)

    return character

def list_character(db: Session, case_id: str) -> list[Character]:
    statement = (
        select(Character)
        .where(Character.case_id == case_id)
        .order_by(Character.name)
    )
    return list(db.exec(statement).all())


def get_character(db: Session, character_id: str) -> Character | None:
    return db.get(Character, character_id)