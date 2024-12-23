from sqlalchemy import Column, Integer, String, DateTime
from base.base import Base

class Chat(Base):
    __tablename__ = "chat"

    cc_id = Column(Integer, primary_key=True, autoincrement=True)
    chat_context = Column(String(5000), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    type = Column(Integer, nullable=False)