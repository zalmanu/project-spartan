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

from __future__ import unicode_literals

from django import forms
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
        if User.objects.filter(email=email) and self.user.email != email:
            raise forms.ValidationError("This email already exists")
        return email

    def clean_username(self):
        user_name = self.cleaned_data['username']
        if User.objects.filter(username=user_name).count() and \
           self.user.username != user_name:
            raise forms.ValidationError("This username already exists")
        return user_name


class Account_Edit(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['city', 'country', 'phone', 'profile_image']
        widgets = {
            'city': forms.Select(attrs={'class':
                                        'form-control input-lg m-bot15',
                                        'id': 'choose_category'}),
            'country': forms.Select(attrs={'class':
                                           'form-control input-lg m-bot15',
                                           'id': 'choose_category'}),
            'phone': forms.TextInput(attrs={'required': 'required'})
        }
