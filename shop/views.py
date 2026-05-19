from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request, slug=None):
    category = None
    products = Product.objects.filter(available=True)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    context = {"category":category,"products": products,}
    return render(request, "shop/product_list.html", context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True,)
    context = {"product": product,}
    return render(request, "shop/product_detail.html", context,)
