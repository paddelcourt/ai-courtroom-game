from pydantic import BaseModel, ConfigDict


class TestimonyStatementBase(BaseModel):
    text: str
    order_index: int


class TestimonyStatementCreate(TestimonyStatementBase):
    case_id: str
    character_id: str


class TestimonyStatementRead(TestimonyStatementBase):
    id: str
    case_id: str
    character_id: str

    model_config = ConfigDict(from_attributes=True)
