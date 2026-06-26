from uuid import uuid4

from sqlmodel import Field, SQLModel


class TestimonyStatement(SQLModel, table=True):
    __tablename__ = "testimony"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    character_id: str = Field(index=True, foreign_key="characters.id")
    case_id: str = Field(foreign_key="cases.id", index=True)
    text: str
    order_index: int = Field(index=True)
