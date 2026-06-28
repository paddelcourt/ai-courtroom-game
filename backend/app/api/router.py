from fastapi import APIRouter

from app.api import cases, health, testimony, characters

api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(cases.router, prefix="/cases", tags=["cases"])
api_router.include_router(testimony.router, prefix="/testimony", tags=["testimony"])
api_router.include_router(characters.router, prefix="/characters", tags=["characters"])
