from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from app.config import settings

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def send_message(to: str, message: str):

    print("TWILIO FROM:", settings.TWILIO_WHATSAPP_NUMBER)
    print("TWILIO TO:", to)
    print("MESSAGE:", message)

    client.messages.create(
        from_=settings.TWILIO_WHATSAPP_NUMBER,
        body=message,
        to=to
    )

def create_response(message: str):
    """
    Creates a response for the actual number that asked
    """

    response = MessagingResponse()
    response.message(message)

    return str(response)