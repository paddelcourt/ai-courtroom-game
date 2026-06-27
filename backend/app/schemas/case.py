from pydantic import BaseModel, ConfigDict


class CaseBase(BaseModel):
    title: str
    description: str | None = None


class CaseCreate(CaseBase):
    pass


class CaseRead(CaseBase):
    id: str
    status: str

    model_config = ConfigDict(from_attributes=True)
