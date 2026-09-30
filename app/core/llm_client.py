import json
from groq import AsyncGroq
from sqlalchemy.orm import Session
from app.config import settings
from app.core.prompts import SYSTEM_PROMPT
from app.services.properties_service import search_properties

client = AsyncGroq(api_key=settings.GROQ_API_KEY)
model = "openai/gpt-oss-120b"

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_properties",
            "description": "Search for properties based on the user's query.",
            "parameters": {
                "type": "object",
                "properties": {
                    "zone": {"type": "string", "description": "Zona o barrio, ej: 'Norte'"},
                    "max_price": {"type": "number", "description": "Precio máximo en euros"},
                    "habitaciones_min": {"type": ["integer", "null"], "description": "Mínimo de habitaciones. Puede ser null si el usuario no lo especifica."}
                },
            },
        }
    }
]

async def generate_response(message: str, db: Session) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": message}
    ]

    while True: 
        print("TOOLS ENVIADAS A GROQ:")
        print(TOOLS)
        response = await client.chat.completions.create(
            model=model,
            tools=TOOLS,
            messages=messages
        )

        msg = response.choices[0].message

        if not msg.tool_calls:
                return msg.content
        
        messages.append(msg)

        for tool_call in msg.tool_calls:
            args = json.loads(tool_call.function.arguments)
            result = search_properties(db, **args)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })