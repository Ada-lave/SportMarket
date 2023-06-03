from .views import *
from django.urls import path
from apps.cart.views import *
urlpatterns = [
    path('', TestDate, name='mainpage'),
    path('cart/', showCart, name='cart'),
    path('search/', searhInMainPage, name='searh')
]
