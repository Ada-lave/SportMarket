from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def test(request):
    return render(request, 'test.html')

def TestDate(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'main.html', context)


def searhInMainPage(request):
    qer = request.GET.get('q')
    products = Product.objects.filter(title__contains=qer)
    context = {
        'products': products
    }
    return render(request, 'search.html', context)


def categoryDetail(request, slug):
    cat = get_object_or_404(Category, slug=slug)
    catName = Category.objects.get(slug = slug).title
    products = cat.product.all()

    context = {
        "products" : products,
        "categoryName":catName
    }

    return render(request, 'category_detail.html', context)


def productDetail(request, category_slug, product_slug):

    cat = get_object_or_404(Category, slug=category_slug)
    product = cat.product.get(slug=product_slug)

    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)
