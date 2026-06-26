from uuid import uuid4

from sqlmodel import Field, SQLModel


class Case(SQLModel, table=True):
    __tablename__ = "cases"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    title: str
    description: str | None = None
    status: str = Field(default="open", index=True)
