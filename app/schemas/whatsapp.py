from pydantic import BaseModel

class TwilioWebhookPayload(BaseModel):
    From: str
    Body: str