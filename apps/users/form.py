from django import forms

class LoginForm(forms.Form):
    user_name = forms.CharField(required=True,min_length=3)
    password = forms.CharField(required=True,min_length=3)
