# app/schemas/analytics_schema.py
from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.models.chat_logs_model import MessageType

class AnalyticsSummary(BaseModel):
    total_messages: int
    distinct_users: int
    avg_response_time_ms: float | None = None

class ChatLogItem(BaseModel):
    id: int
    user_id: str
    message: str
    message_type: MessageType
    timestamp: datetime
    response_time_ms: float | None = None

    model_config = ConfigDict(from_attributes=True)