from sqlmodel import Field, SQLModel

class DefenseChoice(SQLModel, table=True):
    __tablename__ = "defense_choice"
    id: int | None = Field(primary_key=True, index=True)
    testimony_statement_id: int = Field(default=None, index=True, foreign_key="testimony.id")
    text: str = Field()
    is_correct: bool = Field()
    feedback: str = Field()
    


