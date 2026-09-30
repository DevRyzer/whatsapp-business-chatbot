from app.config import settings
from twilio.rest import Client
import json

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

message = client.messages.create(
    from_=settings.TWILIO_WHATSAPP_NUMBER,
    to="whatsapp:+34611647841",
    content_sid="HXe2e105f38b21530c174ee1f85bb7ad5d",
    content_variables='{"1": "29 September 2026", "2": "20:30"}'
)

print("SID:", message.sid)
print("STATUS:", message.status)

