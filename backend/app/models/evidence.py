from sqlmodel import Field, SQLModel

class Evidence(SQLModel, table=True):
    __tablename__ = "evidence"
    id: int | None = Field(primary_key=True, index=True)
    name: str = Field()
    case_id: int = Field(foreign_key="cases.id")
    description: str = Field()
    


