from fastapi import FastAPI
from app.api.v1 import chat, health, analytics

# print("🔑 Loaded OpenAI Key:", settings.openai_api_key)
app = FastAPI()

app.include_router(health.router)
app.include_router(chat.router, tags=["Chat"])
app.include_router(analytics.router, prefix="/v1", tags=["Analytics"])
