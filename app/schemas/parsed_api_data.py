from pydantic import BaseModel

class IncomingMessage(BaseModel):
    message_id: str
    phone_number: str
    text: str
    message_type: str