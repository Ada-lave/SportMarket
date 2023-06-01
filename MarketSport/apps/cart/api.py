import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from apps.cart.cart import Cart

from apps.store.models import Product


def apiAddToCart(request):
    data = json.loads(request.body)
    qua = data['quantity']
    id = data['id']
    update = data['update']

    cart = Cart(request)

    product = get_object_or_404(Product, pk=id)

    if update==False:
        cart.add(product=product, quantity=qua, update_q=False)
        print(cart.__dict__)
        return JsonResponse({"AddtoCart":True})
    else:
        return JsonResponse({"status":'bad'})