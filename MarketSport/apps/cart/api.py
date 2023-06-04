import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from apps.cart.cart import Cart

from apps.store.models import Product

def test(request):
    return JsonResponse({"resp":'resl'})

def apiAddToCart(request):
    print(request)
    data = json.loads(request.body)
    qua = data['quantity']
    id = data['id']
    update = data['update']

    cart = Cart(request)

    product = get_object_or_404(Product, pk=id)

    if update == False:
        cart.add(product=product, quantity=qua, update_q=False)
        print(cart.__dict__)

        print(len(cart))
        return JsonResponse({"AddtoCart": True})
    else:
        return JsonResponse({"status": 'bad'})


def apiIncrementCart(request):
    data = json.loads(request.body)
    id = data['id']

    cart = Cart(request)
    cart.increment(str(id))
    
    return JsonResponse({'success': 'incerement'})

def apiDecrementCart(request):
    data = json.loads(request.body)
    id = data['id']

    cart = Cart(request)
    cart.decrement(str(id))

    return JsonResponse({"success":"decrement"})
