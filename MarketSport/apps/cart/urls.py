from .views import *
from django.urls import path
from .api import apiAddToCart, apiIncrementCart, apiDecrementCart
from .views import *

urlpatterns = [
    path('add', apiAddToCart),
    path('inc', apiIncrementCart),
    path('dec', apiDecrementCart)

]
