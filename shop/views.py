from django.shortcuts import render, get_object_or_404
from shop.models import Category
from shop.services.product_service import retrieve_product
from shop.selectors.product_selector import (get_products,get_similar_products,)


def product_list(request):
    products = get_products(request.GET)

    return render(request,"shop/product_list.html",{"products": products,"search_query": request.GET.get("search", ""),},)


def product_detail(request, id, slug):
    product = retrieve_product(id, slug)

    similar_products = get_similar_products(product)

    return render(request,"shop/product_detail.html",{"product": product,"similar_products": similar_products,},)


def product_list_by_category(request, slug):
    category = get_object_or_404(Category,slug=slug,)

    products = get_products(request.GET).filter(category=category)

    return render(request,"shop/product_list.html",{"products": products,"category": category,"search_query": request.GET.get("search", ""),},)