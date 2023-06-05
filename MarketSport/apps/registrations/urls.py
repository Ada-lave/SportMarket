from .views import *
from django.urls import path
urlpatterns = [
    path('reg/',registration, name='reg'),
]