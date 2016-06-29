from django import forms
from django.db import models
from captcha.fields import ReCaptchaField


class ContactUS(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=1000, null=True)


class CreateContact(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = ContactUS
        fields = '__all__'
