from shop.selectors.product_selector import (get_product_by_id_and_slug, get_products)

def list_products():
    return get_products()


def retrieve_product(id, slug):
    return get_product_by_id_and_slug(id, slug)