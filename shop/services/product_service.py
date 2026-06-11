from shop.selectors.product_query import (
    get_products,
    get_product_by_id_and_slug,
    get_similar_products
)


def list_products(query_params=None):
    return get_products(query_params)


def retrieve_product(product_id, slug):
    return get_product_by_id_and_slug(product_id, slug)


def list_similar_products(product):
    return get_similar_products(product)