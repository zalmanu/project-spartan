from django import forms 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(), label='Password')

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username')
    email = forms.CharField(max_length=100, label='Email', widget=forms.EmailInput())
    password = forms.CharField(max_length=160, min_length=8, label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=160,min_length=8, label='Retype password', widget=forms.PasswordInput())
    country = forms.CharField(max_length=36, label='Country')
    city = forms.CharField(max_length=100, label='City')
    phone = forms.IntegerField(label='Phone number')

    
class PasswordResetForm(forms.Form):
    oldpass = forms.CharField(max_length=160, min_length=8, label="Old password", widget=forms.PasswordInput())
    pass1 = forms.CharField(max_length=160, min_length=8, label="New password",widget=forms.PasswordInput())
    pass2 = forms.CharField(max_length=160, min_length=8, label="Type again the new password", widget=forms.PasswordInput())

