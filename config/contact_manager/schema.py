from datetime import datetime
from ninja import Schema

class ContactSchema(Schema):
    first_name: str
    last_name: str
    phone: str
    email: str
    address: str
    city: str
    state: str

class NotFoundSchema(Schema):
    message: str


class ContactUpdateSchema(Schema):
    first_name: str
    last_name: str
    birthday: datetime
    phone: str
    email: str
    address: str
    city: str
    state: str
    zip_code: str
    country: str