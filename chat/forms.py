from django import forms
from .models import Message


class CreateMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']

    def clean_message(self):
        message = self.cleaned_data['message']
        if not message:
            raise forms.ValidationError("The message is empty")
        return message
