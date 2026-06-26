from uuid import uuid4

from sqlmodel import Field, SQLModel


class Evidence(SQLModel, table=True):
    __tablename__ = "evidence"

    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True, index=True)
    name: str
    case_id: str = Field(foreign_key="cases.id", index=True)
    description: str | None = None
