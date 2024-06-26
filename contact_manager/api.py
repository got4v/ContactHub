from ninja import NinjaAPI, Router
from typing import List
from contact_manager.schema import ContactSchema, NotFoundSchema
from contact_manager.models import Contact
from django.shortcuts import get_object_or_404

api = NinjaAPI()

router = Router()

@router.get("/contacts/", response=List[ContactSchema])
def list_contacts(request):
    contacts = Contact.objects.all()
    return contacts

@router.get("/contacts/{contact_id}", response={200: ContactSchema, 404: NotFoundSchema})
def get_contact(request, contact_id: int):
    contact = get_object_or_404(Contact, id=contact_id)
    return contact

@router.delete("/contacts/{contact_id}", response={204: None, 404: NotFoundSchema})
def delete_contact(request, contact_id: int):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return 204, None

api.add_router("/", router)