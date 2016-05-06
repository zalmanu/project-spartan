from __future__ import unicode_literals

from django import forms
from django.forms import ModelForm, Textarea
from django.db import models
from django.contrib.auth.models import User

class User_Edit(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
    
    def clean_email(self):
        user_email = self.cleaned_data['email']
        username = self.cleaned_data.get('username')
        if email User.objects.objects.filter(email=email).exclude(username):
            raise forms.ValidationError("This email already exists")

    def clean_username(self):
        user_name = self.cleaned_data['username']
        if User.objects.filter(username=user_name).exists():
            raise forms.ValidationError("This username already exists")

