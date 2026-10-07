from app.config import settings
from groq import AsyncGroq

client = AsyncGroq(api_key=settings.GROQ_API_KEY)

