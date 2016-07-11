# Copyright 2015-2016 Emanuel Covaci, Fineas Silaghi, Sebastian Males
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

import hashlib

from django import forms
from django.shortcuts import get_object_or_404
from categories.models import Category
from .models import Spartan


class CreateSpartanForm(forms.ModelForm):

    category = forms.ChoiceField(choices=[(x, x)
                                          for x in Category.categories()])

    class Meta:
        model = Spartan
        fields = ['first_name', 'last_name', 'birthday', 'address',
                  'cnp', 'series', 'cui', 'bank', 'category']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateSpartanForm, self).__init__(*args, **kwargs)

    def clean_bank(self):
        user = self.user
        if(user.account.has_related_object()):
            raise forms.ValidationError("User is already a spartan")
        bank_account = self.cleaned_data['bank']
        if len(bank_account) != 16:
            raise forms.ValidationError("Bank account must be"
                                        " 16 characters long")
        else:
            bank_account = hashlib.sha224(bank_account).hexdigest()
        return bank_account

    def clean_category(self):
        cat_name = self.cleaned_data['category']
        category = get_object_or_404(Category, name=cat_name)
        return category
