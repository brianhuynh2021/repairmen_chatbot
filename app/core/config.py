# app/core/config.py
from __future__ import annotations
import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, model_validator
from app.models.llm_provider_model import LLMProvider

ENV = os.getenv("ENV", "local")
ENV_FILE = {"production": ".env.production", "test": ".env.test", "local": ".env"}.get(ENV, ".env")
BASE_DIR = Path(__file__).resolve().parents[2]
DEFAULT_LOCAL_SQLITE = f"sqlite+aiosqlite:///{(BASE_DIR / 'repairmen_local.db').as_posix()}"

class Settings(BaseSettings):
    env: str = ENV

    llm_provider: LLMProvider = LLMProvider.OPENAI
    openai_api_key: SecretStr
    openai_model: str = "gpt-4"
    gemini_api_key: SecretStr | None = None
    gemini_model: str = "models/gemini-1.5-pro"
    bedrock_region: str = "us-west-2"
    bedrock_model_id: str = "anthropic.claude-v2"

    database_url: str | None = None

    model_config = SettingsConfigDict(
        env_file=str((BASE_DIR / ENV_FILE).resolve()),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @model_validator(mode="after")
    def _fill_or_require_db_url(self) -> "Settings":
        if not self.database_url:
            if self.env in ("local", "test"):
                self.database_url = DEFAULT_LOCAL_SQLITE
            else:
                raise ValueError("DATABASE_URL is required for non-local environments.")
        return self

settings = Settings()
