from django.db.models import QuerySet
from shop.models import Product
from shop.services.search_service import search_products
from shop.services.filters_service import filter_products_by_price


def get_products(query_params=None) -> QuerySet:
    """
    Main Query Engine for Product
    Single source of truth for all product queries
    """

    qs = Product.objects.select_related("category").filter(is_active=True)

    if not query_params:
        return qs

    # search layer
    qs = search_products(qs, query_params.get("search"))

    # price filter layer
    qs = filter_products_by_price(qs,query_params.get("min_price"),query_params.get("max_price"))

    return qs


def get_product_by_id_and_slug(product_id: int, slug: str):
    return Product.objects.select_related("category").get(id=product_id,slug=slug,is_active=True)


def get_similar_products(product, limit=5):
    return Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id)[:limit]