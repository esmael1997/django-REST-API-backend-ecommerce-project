from shop.models import Product
from shop.services.search_service import search_products
from shop.services.filters_service import filter_products_by_price


def get_products(query_params=None):
    queryset = Product.objects.filter(available=True)

    if not query_params:
        return queryset

    queryset = search_products(queryset,query_params.get("search"))

    queryset = filter_products_by_price(queryset,query_params.get("min_price"),query_params.get("max_price"),)

    return queryset


def get_product_by_id_and_slug(id, slug):
    return Product.objects.get(id=id,slug=slug,available=True,)


def get_similar_products(product, limit=5):
    return Product.objects.filter(category=product.category,available=True,).exclude(id=product.id)[:limit]