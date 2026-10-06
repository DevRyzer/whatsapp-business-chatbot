from pydantic import BaseModel, Field
from typing import Optional
"""

This file defines the schemas of the data objects gived by the WhatsApp API, so 

"""
class WhatsAppWebHook(BaseModel):
    object: str
    entry: list[WhatsAppEntry]


class WhatsAppEntry(BaseModel):
    id: str
    changes: list[WhatsAppChanges]

class WhatsAppChanges(BaseModel):
    field: str
    value: WhatsAppValue

class WhatsAppValue(BaseModel):
    messaging_product: str
    metadata: ValueMetadata
    contacts: list[ValueContacts]
    messages: list[WhatsAppMessage]

class WhatsAppMessage(BaseModel):
    id: str
    from_: str = Field(alias="from")
    from_user_id = str
    type: str
    text: Optional[WhatsAppText] = None

class WhatsAppText(BaseModel):
    body: str


"""

subclasses below 

"""


class ValueMetadata(BaseModel):
    display_phone_number: str
    phone_number_id: str

class ValueContacts(BaseModel):
    profile: dict[ProfileName]
    wa_id: str
    user_id: str

class ProfileName(BaseModel):
    name: str