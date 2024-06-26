import json
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from contact_manager.models import Contact

class Command(BaseCommand):
    help = 'Import contacts from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='config/data/contacts.json')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        # Process the data
        for contact_data in data:
            # Example assuming JSON structure: {"first_name": "John", "last_name": "Doe", ...}
            # Adjust field names as per your JSON structure
            contact = Contact(
                first_name=contact_data['first_name'],
                last_name=contact_data['last_name'],
                phone=contact_data.get('phone', None),
                email=contact_data['email'],
                address=contact_data.get('address', None),
                city=contact_data.get('city', None),
                state=contact_data.get('state', None),
            )
            contact.save()

        self.stdout.write(self.style.SUCCESS(f"Successfully imported contacts from {file_path}"))