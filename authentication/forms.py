from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'john_doe'}))
    password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '*****'}))