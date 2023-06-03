from django.shortcuts import render
from .cart import Cart

def showCart(request):
    cart = Cart(request)
    productstr = []
    for item in cart:
        product = item['product']
        b = {'id':product.id, 'title':product.title, 'price':product.price,'quantity':item['quantity']}

        productstr.append(b)
        print(productstr)

    
    return render(request, 'cart.html', {'cart':cart,'productstr':productstr})

