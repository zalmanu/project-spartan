from django import forms
from captcha.fields import ReCaptchaField
from .models import ContactUs

class CreateContact(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = ContactUs
        fields = '__all__'
