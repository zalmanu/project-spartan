from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ContactUs(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = PhoneNumberField(null=True)
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=1000, null=True)


