from apps.cart.cart import Cart
from apps.order.models import *
from apps.store.models import Product


def checkout(request,  address):
    print(request.user.__dict__)
    order = Order(name=request.user.get_full_name(), mobile=request.user.profile.mobile, \
                  email=request.user.email, address=address)
    order.save()

    cart = Cart(request)

    for item in cart:
        product = Product.objects.get(pk=item['id'])
        OrderItem.objects.create(order=order, product=product, price=item['price'], quantity=item['quantity'])
        
    return order.id