from fastapi import APIRouter, Request, Depends, Response
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.whatsapp_service import message_process
from app.config import settings
import json

router = APIRouter()

@router.post("/webhook/whatsapp")
async def whatsapp_webhook(request: Request, db: Session = Depends(get_db)):

    print("LATENEMOS")
    data = await request.json()
    # number = data["value"]["messages"][0]["from"]
    # message = data["value"]["messages"][0]["text"]["body"]
    
    print(json.dumps(data, indent=4))

    return Response(status_code=200)

    #response = await message_process(number=number, message=message, db = db)

    print("RESPONSE: ", response)
    return Response(
        content=response,
        media_type="application/xml"
    )

@router.get("/webhook/whatsapp")
async def verify_webhook(request: Request):
    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == settings.META_VERIFY_TOKEN:
        return Response(content=challenge, media_type="text/plain")

    return Response(content="Forbidden", status_code=403)