from sqlalchemy.orm import Session
from app.core.twilio_client import create_response
from app.core.twilio_client import send_message

async def message_process(number: str, message: str, db: Session):

    return