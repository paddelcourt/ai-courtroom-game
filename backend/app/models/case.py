from sqlmodel import Field, SQLModel

class Case(SQLModel, table=True):
    __tablename__ = "cases"
    id: int | None = Field(primary_key=True, index=True)
    title: str = Field()
    description: str = Field()
    status: str = Field(default="open", index=True)
