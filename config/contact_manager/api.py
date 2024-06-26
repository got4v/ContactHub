from ninja import NinjaAPI, Router
from typing import List
from contact_manager.schema import ContactSchema, NotFoundSchema, ContactUpdateSchema
from contact_manager.models import Contact

api = NinjaAPI()

router = Router()

@router.get("/contacts/", response=List[ContactSchema])
def list_contacts(request):
    contacts = Contact.objects.all()
    return contacts


@router.get("/contacts/{contact_id}", response={200: ContactSchema, 404: NotFoundSchema})
def get_contact(request, contact_id: int):
    try:
        contact = Contact.objects.get(pk=contact_id)
        return 200, ContactSchema(
            id=contact.id,
            first_name=contact.first_name,
            last_name=contact.last_name,
            phone=contact.phone,
            email=contact.email,
            address=contact.address,
            city=contact.city,
            state=contact.state,
        )
    except Contact.DoesNotExist:
        return 404, NotFoundSchema(message="Contact not found.")


api.add_router("/", router)