from django import forms

from .models import Offer


class CreateOfferForm(forms.ModelForm):

    kind = forms.ChoiceField(choices=[(x, x) for x in ['/job', '/hour']])

    class Meta:
        model = Offer
        fields = ['price', 'kind']

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
