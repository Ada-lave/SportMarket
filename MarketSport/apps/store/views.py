from django.shortcuts import render
from .models import Product

def TestDate(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'main.html',context)

def searhInMainPage(request):
    qer = request.GET.get('q')
    products = Product.objects.filter(title__contains=qer)
    context = {
        'products': products
    }
    return render (request, 'main.html', context)
