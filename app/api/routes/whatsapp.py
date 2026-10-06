from fastapi import APIRouter, Request, Depends, Response
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.whatsapp_service import message_process
from app.config import settings
import json

router = APIRouter()

@router.post("/webhook/whatsapp")
async def whatsapp_webhook(request: Request, db: Session = Depends(get_db)) -> Response:

    form = await request.form()
    number = form.get("From")
    message = form.get("Body")

    response = await message_process(number=number, message=message, db=db)

    return Response(
        content=response,
        media_type="application/xml"
    )

@router.post("webhook/whatsapp/status")
async def whatsapp_status(request: Request, db: Session = Depends(get_db)):

    form = await request.form()

    print("FORM STATUS", dict(form))

    return

@router.get("/webhook/whatsapp")
async def verify_webhook(request: Request):
    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == settings.META_VERIFY_TOKEN:
        return Response(content=challenge, media_type="text/plain")

    return Response(content="Forbidden", status_code=403)