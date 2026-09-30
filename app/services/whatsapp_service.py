from sqlalchemy.orm import Session
from app.core.llm_client import generate_response
from app.core.twilio_client import create_response
from app.core.twilio_client import send_message

async def message_process(number: str, message: str, db: Session):
    response = await generate_response(message=message, db=db)
    message = create_response(message=response)

    return message