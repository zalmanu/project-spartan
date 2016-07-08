from django.shortcuts import get_object_or_404
from django import forms
from .models import Announcement
from categories.models import Category


class EditPostForm(forms.ModelForm):

    city = forms.ChoiceField(choices=[(x, x) for x in ['Timisoara']])
    country = forms.ChoiceField(choices=[(x, x) for x in ['Romania']])

    class Meta:
        model = Announcement
        fields = ['title', 'text', 'address', 'country',
                  'city', 'data', 'timePost', 'money']


class CreatePostForm(forms.ModelForm):

    city = forms.ChoiceField(choices=[(x, x) for x in ['Timisoara']])
    country = forms.ChoiceField(choices=[(x, x) for x in ['Romania']])
    category = forms.ChoiceField(choices=[(x, x)
                                          for x in Category.categories()])

    class Meta:
        model = Announcement
        fields = ['title', 'text', 'address', 'country',
                  'city', 'data', 'timePost', 'money', 'category']

    def clean_category(self):
        category = get_object_or_404(Category,
                                     name=self.cleaned_data['category'])
        return category

    def clean_money(self):
        money = self.cleaned_data['money']
        if money < 1 or money > 9223372036854775807:
            raise forms.ValidationError('Enter a valid price')
        return money
