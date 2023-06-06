from .views import *
from django.urls import path
from .api import apiAddToCart, apiIncrementCart, apiDecrementCart, apiRemoveFromCart
from .views import *

urlpatterns = [
    path('add', apiAddToCart),
    path('del', apiRemoveFromCart),
    path('inc', apiIncrementCart),
    path('dec', apiDecrementCart)

]
