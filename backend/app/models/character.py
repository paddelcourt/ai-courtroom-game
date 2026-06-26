from enum import Enum
from uuid import uuid4

from sqlmodel import Field, SQLModel


class CharacterRole(str, Enum):
    WITNESS = "witness"
    PROSECUTOR = "prosecutor"
    DEFENDANT = "defendant"
    DEFENSE_ATTORNEY = "defense_attorney"
    JUDGE = "judge"



class Character(SQLModel, table=True):
    __tablename__ = "characters"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    case_id: str = Field(index=True, foreign_key="cases.id")
    name: str
    status: str = Field(default="open", index=True)
    role: CharacterRole = Field(index=True)
    description: str | None = None

