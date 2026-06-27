from sqlmodel import Session, select

from app.models.evidence import Evidence
from app.schemas.evidence import EvidenceCreate


def create_evidence(db: Session, payload: EvidenceCreate) -> Evidence:
    evidence = Evidence(
        case_id=payload.case_id,
        name=payload.name,
        description=payload.description,
    )

    db.add(evidence)
    db.commit()
    db.refresh(evidence)

    return evidence

def list_evidence(db: Session, case_id: str) -> list[Evidence]:
    return list(db.exec(select(Evidence).where(Evidence.case_id == case_id)).all())


def get_evidence(db: Session, evidence_id: str) -> Evidence | None:
    return db.get(Evidence, evidence_id)