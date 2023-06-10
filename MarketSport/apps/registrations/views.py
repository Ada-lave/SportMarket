from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from .forms  import UserRegistrationForm, LoginUserForm
import random
from django.db import IntegrityError



def registrationUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                try:

                    user = User.objects.create_user(username=form.cleaned_data['username'], first_name=form.cleaned_data['first_name']\
                        ,last_name=form.cleaned_data['last_name'], email=form.cleaned_data['email'], password=form.cleaned_data['password1'])

                    profile = Profile(user=user, mobile=form.cleaned_data.get('mobile'), img=f'ProfileImages/{random.randint(1,4)}.png')
                    profile.save()

                    login(request, user)
                    redirect('mainpage')
                except IntegrityError:
                    messages.error(request, 'Имя пользователя уже занято')
            else:
                messages.error(request, 'Убедитесь в том что пароли одинаковы')
    else:
        form = UserRegistrationForm()
    return render(request, 'reg.html', {'form':form})

def siginUser(request):
    if request.method =='GET':
        form = LoginUserForm()
        return render(request, 'sigin.html', {'form':form})
    elif request.method =='POST':
        form = LoginUserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                login(user=user, request=request)
        
                return redirect('mainpage')
            
        messages.error(request, 'Неверно введен пароль или логин')
        return render(request, 'sigin.html', {'form':form})
    

def logoutUser(request):
    logout(request)
    return redirect('mainpage')