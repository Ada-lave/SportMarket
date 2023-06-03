from .views import *
from django.urls import path
from apps.cart.views import *
urlpatterns = [
    ###Основная страница###
    path('', TestDate, name='mainpage'),

    #Подробнее о товаре

    # path('<slug:category_slug>/<slug:product_slug>/'),

    ###Корзина###
    path('cart/', showCart, name='cart'),

    ###Поиск###
    path('search/', searhInMainPage, name='search'),


    ###Категории###
    path('category/<slug:slug>', categoryDetail ,name='category'),


    ###Заглушки для фронта###
    path('product/', productDetail)

]
