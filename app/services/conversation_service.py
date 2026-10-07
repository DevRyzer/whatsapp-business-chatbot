from sqlalchemy import Session
from app.models.conversation import Conversation
from app.services.data_service import parse_conversation_history

def get_history(db: Session, conversation_id: int) -> list[dict]:
    query = db.query(Conversation).filter(Conversation.id == conversation_id)


    return