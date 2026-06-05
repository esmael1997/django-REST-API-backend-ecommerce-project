from django import template
from shop.models import Product

register = template.Library()


@register.inclusion_tag("shop/includes/latest_products.html")
def show_latest_products(count=5):
    products = Product.objects.filter(available=True).order_by("-created_at")[:count]
    return {"latest_products": products}