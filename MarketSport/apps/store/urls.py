from .views import *
from django.urls import path
from apps.cart.views import *
urlpatterns = [
    ###Основная страница###
    path('', TestDate, name='mainpage'),

    #Подробнее о товаре

    path('product/<slug:category_slug>/<slug:product_slug>/', productDetail, name='productDetail'),

    ###Корзина###
    path('cart/', showCart, name='cart'),
    
    path('/page<int:page>', paginationPage, name='pagination'),

    ###Поиск###
    path('search/', searhInMainPage, name='search'),


    ###Категории###
    path('category/<slug:slug>', categoryDetail ,name='category'),


    ###Заглушки для фронта###


]
