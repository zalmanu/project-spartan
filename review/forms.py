from django import forms


class ReviewForm(forms.Form):
    message = forms.CharField(max_length=1000, label="Review-message", required=False)