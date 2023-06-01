from django.shortcuts import render
from .cart import Cart

def showCart(request):
    cart = Cart(request)
    print(cart)
    return render(request, 'cart.html', {'cart':cart})

