from __future__ import unicode_literals

from django import forms
from django.forms import ModelForm, Textarea
from django.db import models
from django.contrib.auth.models import User
from authentication.models import Account

class User_Edit(forms.ModelForm):
            
    class Meta:
        model = User
        fields = ['username', 'email']
        
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(User_Edit, self).__init__(*args, **kwargs)
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if  User.objects.filter(email=email) and self.user.email != email:
            raise forms.ValidationError("This email already exists")
        return email

    def clean_username(self):
        user_name = self.cleaned_data['username']
        print user_name
        if User.objects.filter(username=user_name).count() and self.user.username != user_name:
            raise forms.ValidationError("This username already exists")
        return user_name


class Account_Edit(forms.ModelForm):

    city = forms.ChoiceField(choices=[(x, x) for x in ['Timisoara']])
    country = forms.ChoiceField(choices=[(x, x) for x in ['Romania']])
    class Meta:
        model = Account
        fields = ['city', 'country', 'telefon']
        widgets = {
            'city': forms.Select(attrs={'class': 'form-control input-lg m-bot15',
                                        'id': 'choose_category'}),
            'country': forms.Select(attrs={'class': 'form-control input-lg m-bot15',
                                  'id': 'choose_category'})
        }


