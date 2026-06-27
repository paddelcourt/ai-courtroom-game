from pydantic import BaseModel, ConfigDict


class EvidenceBase(BaseModel):
    name: str
    description: str


class EvidenceCreate(EvidenceBase):
    case_id: str


class EvidenceRead(EvidenceBase):
    id: str
    case_id: str

    model_config = ConfigDict(from_attributes=True)
