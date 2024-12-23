from pydantic import BaseModel
from typing import Literal
from datetime import datetime
# User 스키마
class UserChatBase(BaseModel):
    chat_context: str
    chat_type: Literal[1]
    timestamp: datetime.now

    class Config:
        orm_mode = True

class AiChatBase(BaseModel):
    chat_context: str
    chat_type: Literal[0]
    timestamp: datetime.now

    class Config:
        orm_mode = True
