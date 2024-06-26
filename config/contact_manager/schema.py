from datetime import datetime
from ninja import Schema


class ContactSchema(Schema):
    id: int
    first_name: str
    last_name: str
    phone: str
    email: str
    address: str
    city: str
    state: str

class NotFoundSchema(Schema):
    message: str