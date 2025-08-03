from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: str = "dummy"

    model_config = SettingsConfigDict(env_file=".env")
    #model_config = {"env_file": ".env"}



settings = Settings()
