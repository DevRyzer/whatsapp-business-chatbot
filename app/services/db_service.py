from sqlalchemy.orm import Session
from app.models.conversation import Conversation

def insert_conversation(db: Session, conversation_data: dict) -> None:
    return