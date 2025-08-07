from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

from app.models.llm_provider_model import LLMProvider
class Settings(BaseSettings):
    llm_provider: LLMProvider = LLMProvider.OPENAI
    
    #Openai
    openai_api_key: SecretStr
    openai_model: str = "gpt-3.5-turbo"
    
    # Gemini
    gemini_api_key: str | None = None
    gemini_model: str = "models/gemini-1.5-pro"

    # Bedrock
    bedrock_region: str = "us-west-2"
    bedrock_model_id: str = "anthropic.claude-v2"
    # Robust relative .env loading
    model_config = SettingsConfigDict(
        env_file=".env",  # 👈 đảm bảo là root project có .env
        env_file_encoding="utf-8",
    )

settings = Settings()
