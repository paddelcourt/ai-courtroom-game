from sqlmodel import Field, SQLModel

class TestimonyStatement(SQLModel, table=True):
    __tablename__ = "testimony"
    id: int | None = Field(primary_key=True, index=True)
    character_id: int = Field(index=True, foreign_key="characters.id")
    case_id: int = Field(foreign_key="cases.id", index=True)
    text: str = Field(default=None)
    order_index: int = Field(index=True)
    


