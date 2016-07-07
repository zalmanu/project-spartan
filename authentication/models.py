from __future__ import unicode_literals
import md5

from django import forms
from django.db import models
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField
from phonenumber_field.modelfields import PhoneNumberField

from spartans.models import Spartan


class Account(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=36, null=True)
    phone = PhoneNumberField(null=True)
    code = models.CharField(max_length=100, null=True, blank=True)

    def has_related_object(self):
        has_spartan = False
        try:
            has_spartan = (self.user.spartan is not None)
        except Spartan.DoesNotExist:
            pass
        return has_spartan and (self.user is not None)

    def gravatar_photo(self):
        usshash = md5.new()
        usshash.update(self.user.email)
        return usshash.hexdigest()


class UserRegisterForm(forms.ModelForm):
    retypepassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Retype password',
        'label': 'Retype password',
        'required': 'required'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput({'required': 'required',
                                         'placeholder': 'Username'}),
            'email': forms.EmailInput({'required': 'required',
                                       'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'required': 'required',
                                                   'placeholder': 'Password'})
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError("This email already exists")
        return email

    def clean_username(self):
        user_name = self.cleaned_data['username']
        if User.objects.filter(username=user_name).count():
            raise forms.ValidationError("This username already exists")
        return user_name

    def clean_retypepassword(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['retypepassword']
        if password.isdigit():
            raise forms.ValidationError("Password is entirely numeric")
        if password != password2:
            raise forms.ValidationError("Passwords do not match")
        if len(password) < 8:
            raise forms.ValidationError("Password is too short")
        return password2


class AccountRegisterForm(forms.ModelForm):

    city = forms.ChoiceField(choices=[(x, x) for x in ['Timisoara']])
    country = forms.ChoiceField(choices=[(x, x) for x in ['Romania']])
    captcha = ReCaptchaField()

    class Meta:
        model = Account
        exclude = ['user', 'code']
