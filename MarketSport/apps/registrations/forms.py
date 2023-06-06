from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=120,label='Имя', widget=forms.TextInput(attrs={
        'class': 'place FormReg'
    }))
    last_name = forms.CharField(max_length=120,label='Фамилия', widget=forms.TextInput(attrs={
        'class': 'place FormReg'
    }))
    mobile = forms.CharField(max_length=120,label='Номер', widget=forms.TextInput(attrs={
        'class': 'place FormReg'
    }))
    username = forms.CharField(max_length=120,label='Логин', widget=forms.TextInput(attrs={
        'class': 'place FormReg'
    }))
    email = forms.CharField(max_length=120,label='Почта', widget=forms.TextInput(attrs={
        'class': 'place FormReg'
    }))
    password1 = forms.CharField(max_length=120, label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'place FormReg'
    }))
    password2 = forms.CharField(max_length=120, label='Подтвердите пароль', widget=forms.PasswordInput(attrs={
        'class': 'place FormReg'
    }))

    class Meta:
        model = User
