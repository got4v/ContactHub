from django.db import models

class Contact(models.Model):
    first_name = models.CharField("First Name", max_length=100)
    last_name = models.CharField("Last Name", max_length=100)
    phone = models.CharField("Phone", max_length=20, blank=True, null=True)
    email = models.EmailField("Email", unique=True)
    address = models.TextField("Address", blank=True, null=True)
    city = models.CharField("City", max_length=100, blank=True, null=True)
    state = models.CharField("State", max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


