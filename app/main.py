from fastapi import FastAPI
from app.api.routes.whatsapp import router as whatsapp_router
from app.db.session import engine, Base
from app.models.inmueble import Inmueble

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inmobiliaria Bot")
app.include_router(whatsapp_router)


app.get("/")