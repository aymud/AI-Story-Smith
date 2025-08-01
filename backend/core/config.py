from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

# Note: The .env file needs to match the config.
class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    DATABASE_URL: str = None,
    ALLOWED_ORIGINS: str = ""
    # OPENAI_API_KEY: str = None

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, value: str) -> List[str]:
        return value.split(",") if value else []

    # Set configuration so that Python knows how to correctly load the env file.
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()