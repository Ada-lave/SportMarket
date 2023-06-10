from apps.cart.cart import Cart
from apps.order.models import *
from apps.store.models import Product
from django.core.mail import EmailMessage
from django.utils.html import strip_tags
from django.template.loader import get_template
from django.conf import settings


def checkout(request,  address):
    print(request.user.__dict__)
    order = Order(name=request.user.get_full_name(), mobile=request.user.profile.mobile, \
                  email=request.user.email, address=address)
    order.save()

    cart = Cart(request)

    for item in cart:
        product = Product.objects.get(pk=item['id'])
        OrderItem.objects.create(order=order, product=product, price=item['price'], quantity=item['quantity'])
    

    template = get_template('index1.html')

    prod = []
    tcost = 0
    print(cart.totalCost())
    for item in cart:
        tcost += int(item['price'] * int(item['quantity']))
        prod.append({'price':item['price'], 'title':item['title'], 'quantity':item['quantity']})
    
    products = {"products":prod, 'tcost':tcost}

    content = template.render(products)
    
    email = EmailMessage(subject='Ваш чек от сайта earth-market.ru', body=content, to=[request.user.email])
    email.content_subtype = 'html'
    email.send()
        
    return order.id