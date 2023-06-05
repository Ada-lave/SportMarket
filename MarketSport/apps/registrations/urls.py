from .views import *
from django.urls import path
urlpatterns = [
    path('signup/',registration),
    path('signin/', sigin)
]