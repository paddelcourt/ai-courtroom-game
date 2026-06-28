import json

from sqlmodel import Session

from app.core.config import settings
from app.core.prompt import CASE_GENERATION_SYSTEM_PROMPT, CASE_GENERATION_USER_PROMPT
from app.models.case import Case
from app.schemas.case import CaseCreate
from app.schemas.character import CharacterCreate
from app.schemas.defense_choice import DefenseChoiceCreate
from app.schemas.evidence import EvidenceCreate
from app.schemas.testimony import TestimonyStatementCreate
from app.services.ai_client import client
from app.services.case_service import create_case
from app.services.character_service import create_character
from app.services.defense_choice_service import create_defense_choice
from app.services.evidence_service import create_evidence
from app.services.testimony_service import create_testimony


def case_generation(theme: str = "museum theft") -> dict:
    response = client.responses.create(
        model=settings.AI_GATEWAY_MODEL,
        input=[
            {
                "role": "system",
                "content": CASE_GENERATION_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": CASE_GENERATION_USER_PROMPT.format(theme=theme),
            },
        ],
        text={"format": {"type": "json_object"}},
    )

    return json.loads(response.output_text)

def generate_and_store_case(db: Session, theme: str = "museum theft") -> Case:
    data = case_generation(theme)
    case = create_case(
        db,
        CaseCreate(
            title=data["case"]["title"],
            description=data["case"]["description"],
        ),
    )

    character_key_to_id = {}

    for character_data in data["characters"]:
        character = create_character(
            db,
            CharacterCreate(
                case_id=case.id,
                name=character_data["name"],
                role=character_data["role"],
                description=character_data.get("description"),
            )
        )
        character_key_to_id[character_data["key"]] = character.id

    testimony_key_to_id = {}
    for testimony_data in data["testimony"]:
        character_key = testimony_data["character_key"]
        if character_key not in character_key_to_id:
            raise ValueError(f"Unknown character key from AI response: {character_key}")

        testimony_statement = create_testimony(
            db,
            TestimonyStatementCreate(
                text=testimony_data["text"],
                order_index=testimony_data["order_index"],
                case_id=case.id,
                character_id=character_key_to_id[character_key],
            ),
        )
        testimony_key_to_id[testimony_data["key"]] = testimony_statement.id

        for choice_data in testimony_data["choices"]:
            create_defense_choice(
                db,
                DefenseChoiceCreate(
                    testimony_statement_id=testimony_statement.id,
                    text=choice_data["text"],
                    is_correct=choice_data["is_correct"],
                    feedback=choice_data.get("feedback"),
                    prosecutor_response=choice_data.get("prosecutor_response"),
                    judge_response=choice_data.get("judge_response"),
                )
            )

    for evidence_data in data["evidence"]:
        create_evidence(
            db,
            EvidenceCreate(
                case_id=case.id,
                name=evidence_data["name"],
                description=evidence_data["description"],
            ),
        )

    return case
                                
