from __future__ import unicode_literals

from django import forms
from django.db import models

from spartans.models import Spartan
from posts.models import Announcement


class Offer(models.Model):
    price = models.IntegerField(null=True)
    spartan = models.ForeignKey(Spartan, related_name='bids')
    post = models.ForeignKey(Announcement, related_name='offers')
    status = models.BooleanField(default=False)


class CreateOfferForm(forms.ModelForm):


    class Meta:
        model = Offer
        fields = ['price']

    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop('post', None)
        super(CreateOfferForm, self).__init__(*args, **kwargs)

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0 or price > 9223372036854775807:
            raise forms.ValidationError("Enter a valid price")
        if price > self.post.money:
            raise forms.ValidationError("Price is too high"
                                        " for the employer")
        return price
