from django import forms
from captcha.fields import ReCaptchaField


class ContactUSForm(forms.Form):
    prenume = forms.CharField(max_length=40, label="First name",
                              widget=forms.TextInput(
                                  attrs={'required': 'required'}))
    nume = forms.CharField(max_length=40, label="Last name",
                           widget=forms.TextInput(
                               attrs={'required': 'required'}))
    email = forms.CharField(max_length=100, label='Email',
                            widget=forms.EmailInput(
                                attrs={'required': 'required'}))
    phone = forms.IntegerField(label='Phone number',
                               widget=forms.NumberInput(
                                   attrs={'required': 'required'}))
    message = forms.CharField(max_length=1000, label="Message",
                              widget=forms.TextInput(
                                  attrs={'required': 'required'}))
    captcha = ReCaptchaField()
