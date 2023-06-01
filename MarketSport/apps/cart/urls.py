from .views import *
from django.urls import path
from .api import apiAddToCart
from .views import *

urlpatterns = [
    path('add/', apiAddToCart),
    path('cart', showCart)
]