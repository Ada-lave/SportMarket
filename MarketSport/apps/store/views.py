from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category


def TestDate(request):
    products = Product.objects.all()

    paginator = Paginator(products, 9)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)


    context = {
        'products': page_obj
    }
    return render(request, 'main.html', context)


def paginationPage(request, page):
    products = Product.objects.all()

    paginator = Paginator(products, 9)
    
    page_obj = paginator.get_page(page)


    context = {
        'products': page_obj
    }
    return render(request, 'pagination.html', context)

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

    paginator = Paginator(products, 9)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    

    context = {
        "products" : page_obj,
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
