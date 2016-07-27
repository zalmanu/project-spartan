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

import hashlib
from datetime import date

from django import forms
from django.shortcuts import get_object_or_404
from categories.models import Category
from .models import Spartan


class CreateSpartanForm(forms.ModelForm):

    class Meta:
        model = Spartan
        fields = ['first_name', 'last_name', 'birthday', 'address',
                  'cnp', 'series', 'cui', 'bank', 'category']

    def clean_bank(self):
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

    def clean_cui(self):
        cui = self.cleaned_data['cui']
        valid = True
        if(cui[:2] != "RO"):
            valid = False
        else:
            cui = cui[2:]
            if not cui.isdigit():
                valid = False
            else:
                testing = 753217532
                sum = 0
                if len(cui) > 10 or len(cui) < 6:
                    valid = False

                cui = int(cui)
                c1 = cui % 10
                cui = int(cui / 10)
                while(cui > 0):
                    sum += cui % 10 * testing % 10
                    cui = cui / 10
                    testing = testing / 10
                c2 = sum * 10 % 11
                if(c2 == 10):
                    c2 = 0
                if(c1 == c2):
                    valid = False
        if(not valid):
            raise forms.ValidationError("Enter a valid CUI")
        return cui

    def clean_cnp(self):
        cnp = self.cleaned_data['cnp']
        if(len(cnp) != 13):
            raise forms.ValidationError("CNP is not 13 characters long")
        elif(not cnp.isdigit()):
            raise forms.ValidationError("Invalid CNP")
        return cnp

    def clean_birthday(self):
        birthday = self .cleaned_data['birthday']
        if(birthday > date.today()):
            raise forms.ValidationError("Enter a valid birthday")
        else:
            delta = date.today() - birthday
            if delta.days < 6570:
                raise forms.ValidationError("You have to be at least 18 "
                                            "to be a spartan")
        return birthday
