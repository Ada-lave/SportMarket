from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=120)
    last_name = forms.CharField(max_length=120)
    mobile = forms.CharField(max_length=60)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','mobile','email','password1','password2')
        label = {'first_name':'Имя', 'last_name':'Фамилия',\
                  'mobile':'Номер телефона', 'email':'Email', 'password1':'Пароль', 'password2':'Подтвердите пароль'}
        