from django.shortcuts import render
from .models import Product

def TestDate(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'mainpage.html',context)
