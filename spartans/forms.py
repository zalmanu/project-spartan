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
