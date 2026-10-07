from app.schemas.parsed_api_data import IncomingMessage
from app.schemas.whatsapp_api_data import WhatsAppWebHook


"""def parse_whatsapp_message(webhook: WhatsAppWebHook) -> IncomingMessage:
    message = webhook.entry[0].changes[0].value.messages[0]

    return IncomingMessage (
        message_i = message.id,
        phone_number=message.from_,
        text=message.text.body,
        message_type=message.type
    )"""

def parse_message_data(data, ) -> list[dict]:
    return [{
        "role": message.role,
        "content": message.content
        }
        for message in data.limit(10).all()
    ] 

def parse_property_data(data) -> list[dict]:
    return [
        {
            "direccion": property.direccion,
            "zona": property.zona,
            "precio": property.precio,
            "metros": property.metros_cuadrados,
            "habitaciones": property.habitaciones,
            "descripcion": property.descripcion
        }
        for property in data.all()
    ]