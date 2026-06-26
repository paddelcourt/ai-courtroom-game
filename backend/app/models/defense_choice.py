from uuid import uuid4

from sqlmodel import Field, SQLModel


class DefenseChoice(SQLModel, table=True):
    __tablename__ = "defense_choice"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    testimony_statement_id: str = Field(index=True, foreign_key="testimony.id")
    text: str
    is_correct: bool = Field(default=False)
    feedback: str | None = None
