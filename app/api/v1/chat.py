from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chatbot_service import ChatbotService


router = APIRouter()
chatbot = ChatbotService()

@router.post("/chat", response_model=ChatResponse)
def chat_enpoint(payload: ChatRequest):
    reply = chatbot.get_reply(payload.message)
    return ChatResponse(reply=reply)
