from app.db.session import Base
from sqlalchemy import Column, Integer, String, DateTime

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True)
    phone_number = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)