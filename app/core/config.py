from pydantic_settings import BaseSettings, SettingsConfigDict
import os
class Settings(BaseSettings):
    openai_api_key: str
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
