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
from stdnum import cnp
from stdnum.exceptions import *
from datetime import date

from django import forms
from django.shortcuts import get_object_or_404
from categories.models import Category
from .models import Spartan


class CreateSpartanForm(forms.ModelForm):

    class Meta:
        model = Spartan
        fields = ['first_name', 'last_name', 'birthday', 'address',
                  'cnp', 'series', 'category']

    def clean_category(self):
        cat_name = self.cleaned_data['category']
        category = get_object_or_404(Category, name=cat_name)
        return category

    def clean_birthday(self):
        birthday = self .cleaned_data['birthday']
        if birthday > date.today():
            raise forms.ValidationError("Enter a valid birthday")
        else:
            delta = date.today() - birthday
            if delta.days < 5110:
                raise forms.ValidationError("You have to be at least 14 old"
                                            " to be a spartan")
        return birthday

    def clean_cnp(self):
        form_cnp = self.cleaned_data['cnp']
        try:
            cnp.validate(form_cnp)
            return form_cnp
        except (InvalidFormat, InvalidLength, InvalidChecksum):
            raise forms.ValidationError("Invalid CNP")

    def clean_series(self):
        series = self.cleaned_data['series']
        if len(series) < 8:
            raise forms.ValidationError("Id series is not 8 characters long")
        else:
            if(not series[0:2].isalpha()):
                raise forms.ValidationError("First two digits must be letters")
            if(not series[3:8].isdigit()):
                raise forms.ValidationError("Series number is not numeric")
        return series
