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
import re

from captcha.fields import ReCaptchaField
from django.contrib.auth.models import User
from django import forms
from .models import Account


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username',
                               widget=forms.TextInput(attrs={
                                   'required': 'required',
                                   'placeholder': "Username"}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'required': 'required',
               'placeholder': "Password"}),
                               label='Password')


class PasswordResetForm(forms.Form):
    old_password = forms.CharField(max_length=160, min_length=8,
                                   label="Old password",
                                   widget=forms.PasswordInput(
                                       attrs={'required': 'required'}))
    password_1 = forms.CharField(max_length=160, min_length=8,
                                 label="New password",
                                 widget=forms.PasswordInput(
                                     attrs={'required': 'required'}))
    password_2 = forms.CharField(max_length=160, min_length=8,
                                 label="Type again the new password",
                                 widget=forms.PasswordInput(
                                     attrs={'required': 'required'}))

    def clean_password2(self, request):
        password_old = self.cleaned_data['old_password']
        password_1 = self.cleaned_data['password_1']
        password_2 = self.cleaned_data['password_2']
        if not request.user.check_password(password_old):
            raise forms.ValidationError("Incorrect old password")
        if password_1 != password_2:
            raise forms.ValidationError("Those two password are not the same")
        if password_1.isdigit() and password_2.isdigit():
            raise forms.ValidationError("Password is entirely numeric")
        if len(password_1) < 8:
            raise forms.ValidationError("Password is too short")


class ForGotPassword(forms.Form):
    password_1 = forms.CharField(max_length=160, min_length=8,
                                 label="New password",
                                 widget=forms.PasswordInput(
                                     attrs={'required': 'required'}))
    password_2 = forms.CharField(max_length=160, min_length=8,
                                 label="Type again the new password",
                                 widget=forms.PasswordInput(
                                     attrs={'required': 'required'}))


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
        elif(
                re.match(r"^[\w.@+-]+$", user_name) or user_name.isdigit()
        ):
            raise forms.ValidationError("Username contains invalid characters")
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
        fields = ['profile_image', 'phone', 'city', 'country']
