from django.shortcuts import render
from django.contrib.auth import login

from .forms  import UserRegistrationForm

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()

            password = form.cleaned_data.get('password1')
            login(request,user)

    else:
        form = UserRegistrationForm()
    return render(request, 'reg.html', {'form':form})

def sigin(request):
    return render(request, 'sigin.html')