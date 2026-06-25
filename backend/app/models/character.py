from typing import Annotated, Optional, List
from enum import Enum
from sqlmodel import Field, SQLModel


class CharacterRole(str, Enum):
    WITNESS = "witness"
    PROSECUTOR = "prosecutor"
    DEFENDANT = "defendant"
    DEFENSE_ATTORNEY = "defense_attorney"
    JUDGE = "judge"



class Character(SQLModel, table=True):
    __tablename__ = "characters"
    id: int | None = Field( primary_key=True, index=True)
    case_id: int = Field(index=True, foreign_key="cases.id")
    name: str = Field()
    status: str = Field(default="open", index=True)
    role: CharacterRole = Field(index=True)
    description: str = Field()


