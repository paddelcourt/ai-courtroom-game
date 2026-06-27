from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Courtroom Game API"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "sqlite:///./ai_courtroom_game.db"
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:3000"]
    AI_GATEWAY_API_KEY: str | None = None
    AI_GATEWAY_MODEL: str = "openai/gpt-4.1-mini"
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
