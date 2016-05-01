from django import forms 


class SendMessageForm(forms.Form):
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'textarea' , 
                                                            'placeholder':'Type here!'}))
