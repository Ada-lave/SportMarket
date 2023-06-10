from django.shortcuts import render, redirect
from .cart import Cart
from apps.store.models import Product

def showCart(request):
    cart = Cart(request)
    productstr = []
    productsImgs = []
    for item in cart:
        product = item['product']
        productsImgs.append(Product.objects.get(id=product.id).image1.url)
        
        b = {'id':product.id, 'title':product.title, 'price':product.price,'quantity':item['quantity'],\
              'color':item['color'], 'size': item['size'], 'img':item['img']}

        productstr.append(b)
    print(productsImgs)
    print(productstr)
    


    
    return render(request, 'cart.html', {'cart':cart,'productstr':productstr, 'productImgs':productsImgs})

