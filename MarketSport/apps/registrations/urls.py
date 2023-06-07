from .views import *
from django.urls import path
urlpatterns = [
    path('signup/',registrationUser, name='signup'),
    path('signin/', siginUser, name='signin'),
    path('logout/', logoutUser, name='logout')
]