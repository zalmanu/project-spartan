from __future__ import unicode_literals

from django import forms
from django.forms import ModelForm, Textarea
from django.db import models
from django.contrib.auth.models import User

class User_Edit(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': Textarea(attrs={'value': model.username })
        }
