from sqlalchemy import Column, Integer, Float, String, DateTime, Text
from sqlalchemy import Enum as SAEnum            # ✅ SQLAlchemy Enum
from app.models import Base
from datetime import datetime, timezone
import enum                                   # ✅ stdlib enum

class MessageType(str, enum.Enum):               # ✅ stdlib enum
    user = "user"
    bot = "bot"

class ChatLog(Base):
    __tablename__ = "chat_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False, index=True)
    session_id = Column(String, nullable=True)
    message = Column(Text, nullable=False)

    message_type = Column(
        SAEnum(MessageType, name="message_type_enum"),  # ✅ SQLAlchemy Enum
        nullable=False,
        server_default=MessageType.user.value,
    )
    llm_provider = Column(String, nullable=True)
    status = Column(String, nullable=True)  # e.g., success, error
    env = Column(String, nullable=False, server_default="local")
    timestamp = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    response_time_ms = Column(Float, nullable=True)