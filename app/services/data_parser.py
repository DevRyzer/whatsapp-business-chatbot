from app.schemas.parsed_api_data import IncomingMessage
from app.schemas.whatsapp_api_data import WhatsAppWebHook


def parse_whatsapp_message(webhook: WhatsAppWebHook) -> IncomingMessage:
    message = webhook.entry[0].changes[0].value.messages[0]

    return IncomingMessage (
        message_i = message.id,
        phone_number=message.from_,
        text=message.text.body,
        message_type=message.type
    )