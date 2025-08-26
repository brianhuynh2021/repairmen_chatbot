# app/api/v1/chat.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.concurrency import run_in_threadpool
from sqlalchemy.ext.asyncio import AsyncSession
import time

from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chatbot_service import ChatbotService
from app.models.chat_model import LangChainResult
from app.db.session_async import get_session
from app.models.chat_logs_model import ChatLog, MessageType
from app.core.config import settings

router = APIRouter()
chatbot = ChatbotService()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(
    payload: ChatRequest,
    db: AsyncSession = Depends(get_session),
) -> ChatResponse:
    user_id = payload.user_id or "anon"
    started = time.perf_counter()

    # 1) log user message (received)
    db.add(ChatLog(
        user_id=user_id,
        session_id=None,
        message=payload.message,
        message_type=MessageType.user,
        llm_provider=settings.llm_provider.value,
        status="received",
        env=settings.env,
    ))
    await db.flush()

    try:
        # 2) gọi LLM (get_reply là sync -> chạy trong threadpool)
        result: LangChainResult = await run_in_threadpool(
            chatbot.get_reply, payload.message
        )
        reply_text = result.result

        # 3) log bot reply (success)
        elapsed_ms = (time.perf_counter() - started) * 1000.0
        db.add(ChatLog(
            user_id=user_id,
            session_id=None,
            message=reply_text,
            message_type=MessageType.bot,
            llm_provider=settings.llm_provider.value,
            status="success",
            env=settings.env,
            response_time_ms=elapsed_ms,
        ))
        await db.commit()
        return ChatResponse(reply=reply_text)

    except Exception as e:
        # 4) log bot reply (error)
        elapsed_ms = (time.perf_counter() - started) * 1000.0
        db.add(ChatLog(
            user_id=user_id,
            session_id=None,
            message=str(e),
            message_type=MessageType.bot,
            llm_provider=settings.llm_provider.value,
            status="error",
            env=settings.env,
            response_time_ms=elapsed_ms,
        ))
        await db.commit()
        # tuỳ chọn: ẩn lỗi nội bộ ra ngoài
        raise HTTPException(status_code=500, detail="Chat service error")