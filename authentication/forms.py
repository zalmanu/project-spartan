
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='Username',
                               widget=forms.TextInput(attrs={
                                   'required': 'required'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'required': 'required'}),
                               label='Password')


class PasswordResetForm(forms.Form):
    old_password = forms.CharField(max_length=160, min_length=8,
                                   label="Old password",
                                   widget=forms.PasswordInput(
                                  attrs={'required': 'required'}))
    password_1 = forms.CharField(max_length=160, min_length=8, label="New password",
                                 widget=forms.PasswordInput(
                                attrs={'required': 'required'}))
    password_2 = forms.CharField(max_length=160, min_length=8,
                                 label="Type again the new password",
                                 widget=forms.PasswordInput(
                                attrs={'required': 'required'}))


class ForGotPassword(forms.Form):
    password_1 = forms.CharField(max_length=160, min_length=8, label="New password",
                                 widget=forms.PasswordInput(
                                attrs={'required': 'required'}))
    password_2 = forms.CharField(max_length=160, min_length=8,
                                 label="Type again the new password",
                                 widget=forms.PasswordInput(
                                attrs={'required': 'required'}))
