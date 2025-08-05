from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import chat, health

# print("🔑 Loaded OpenAI Key:", settings.openai_api_key)
app = FastAPI()

app.include_router(health.router)
app.include_router(chat.router, tags=["Chat"])
