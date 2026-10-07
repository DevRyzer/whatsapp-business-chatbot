from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_WHATSAPP_NUMBER: str

    GROQ_API_KEY: str

    DATABASE_URL: str

    META_TOKEN: str
    META_VERIFY_TOKEN: str
    
    PHONE_NUMBER_ID: str
    WHATS_BUSINESS_ACCOUNT_ID: str

    AI_MODEL: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
