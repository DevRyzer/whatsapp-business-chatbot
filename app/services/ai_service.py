import json

from sqlalchemy.orm import Session
from app.config import settings
from app.core.prompts import SYSTEM_PROMPT, MAX_TOOL_ITERATIONS
from app.core.tools import TOOLS
from app.core.llm_client import client
from app.services.properties_service import search_properties

async def generate_response(message: str, db: Session) -> str:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": message}
    ]

    for _ in range (MAX_TOOL_ITERATIONS): 
        response = await client.chat.completions.create(
            model=settings.AI_MODEL,
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

    raise RuntimeError("Max tool-calling iterations exceeded.")