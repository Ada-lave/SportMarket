from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .models import Profile

from .forms  import UserRegistrationForm

def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'mod':user.profile.mobile})

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            profile = Profile(user=user, mobile=form.cleaned_data.get('mobile'))
            profile.save()

            login(request, user)
            redirect('mainpage')
    else:
        form = UserRegistrationForm()
    return render(request, 'reg.html', {'form':form})

def sigin(request):
    return render(request, 'sigin.html')