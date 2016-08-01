# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.
from django.core.validators import validate_email
from django import forms

from captcha.fields import ReCaptchaField
from .models import ContactUs


class CreateContact(forms.ModelForm):

    captcha = ReCaptchaField()

    class Meta:
        model = ContactUs
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput({'required': 'required',
                                       'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'required': 'required',
                                             'placeholder': 'Message'})
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise forms.ValidationError("Enter a valid first name")

    def clean_email(self):
        email = self.clean_data['email']
        if validate_email(email):
            raise forms.ValidationError("Email is not valid")
        return email

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha():
            raise forms.ValidationError("Enter a valid last name")

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 50:
            raise forms.ValidationError(
                "Your contact message has to be at least "
                "50 characters long")
