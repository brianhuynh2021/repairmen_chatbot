from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    message: str
    user_id: Optional[str] = None # For first phase not compulsory
    
class ChatResponse(BaseModel):
    reply: str
