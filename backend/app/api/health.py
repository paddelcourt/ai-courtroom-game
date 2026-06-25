from fastapi import APIRouter

from app.schemas.health import HealthCheck

router = APIRouter()


@router.get("", response_model=HealthCheck)
def read_health() -> HealthCheck:
    return HealthCheck(status="ok")
