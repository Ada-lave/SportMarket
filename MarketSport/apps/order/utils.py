from apps.cart.cart import Cart
from apps.order.models import *
from apps.store.models import Product
from django.core.mail import send_mail
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
    
    text = f"Ваш заказ оформлен\nОбщая стоимость {cart.totalCost()}\nТовары которые вы выбрали:\n"
    for item in cart:
        text += f"{item['title']} {item['quantity']}шт\n"
    send_mail(f"{request.user.get_full_name()} ваш заказ успешно оформлен" ,f"{text}\n Вам в скором времени перезвонить менеджер что бы подтвердить ваш заказ.",settings.EMAIL_HOST_USER, [request.user.email])
    
        
    return order.id