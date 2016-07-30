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

from django import forms

from .models import Offer


class CreateOfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = ['price']

    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop('post', None)
        super(CreateOfferForm, self).__init__(*args, **kwargs)

    def clean_price(self):
        price = self.cleaned_data['price']
        if price > self.post.money:
            raise forms.ValidationError("Price is too high"
                                        " for the employer")
        return price
