from urllib import request
from django.core import paginator
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator

def product_list(request, slug=None):
    category = None
    products = Product.objects.filter(available=True)

    paginator = Paginator(products, 3)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)


    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    context = {"category":category,"products": page_obj,"page_obj": page_obj,}
    return render(request, "shop/product_list.html", context)

def product_detail(request, id, slug):
    products = Product.objects.filter(available=True)

    paginator = Paginator(products, 3)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)
    context = {"products": page_obj,"page_obj": page_obj,}
    return render(request, "shop/product_detail.html", context,)
