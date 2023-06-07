from .views import *
from django.urls import path
urlpatterns = [
    path('signup/',registrationUser, name='registration'),
    path('signin/', siginUser, name='sigin'),
    path('logout/', logoutUser, name='logout')
]