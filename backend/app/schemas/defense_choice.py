from pydantic import BaseModel, ConfigDict


class DefenseChoiceBase(BaseModel):
    text: str
    is_correct: bool = False
    feedback: str | None = None
    prosecutor_response: str | None = None
    judge_response: str | None = None


class DefenseChoiceCreate(DefenseChoiceBase):
    testimony_statement_id: str


class DefenseChoiceRead(DefenseChoiceBase):
    id: str
    testimony_statement_id: str

    model_config = ConfigDict(from_attributes=True)
