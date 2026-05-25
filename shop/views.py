from django.shortcuts import render
from shop.services.product_service import list_products, retrieve_product


def product_list(request):
    products = list_products()
    return render(request, "shop/product_list.html", {"products": products})


def product_detail(request, id, slug):
    product = retrieve_product(id, slug)
    return render(request, "shop/product_detail.html", {"product": product})
