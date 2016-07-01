from django import forms
from django.db import models
from captcha.fields import ReCaptchaField
from phonenumber_field.modelfields import PhoneNumberField


class ContactUS(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = PhoneNumberField(null=True)
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=1000, null=True)


class CreateContact(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = ContactUS
        fields = '__all__'
