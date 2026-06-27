from pydantic import BaseModel, ConfigDict
from app.models.character import CharacterRole



class CharacterBase(BaseModel):
    name: str
    role: CharacterRole 
    description: str | None = None


class CharacterCreate(CharacterBase):
    case_id: str


class CharacterRead(CharacterBase):
    id: str
    case_id: str
    status: str

    model_config = ConfigDict(from_attributes=True)
