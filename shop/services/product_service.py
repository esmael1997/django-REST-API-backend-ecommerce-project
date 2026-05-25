from shop.selectors.product_selector import (get_available_products,get_product_by_id_and_slug)

def list_products():
    return get_available_products()


def retrieve_product(id, slug):
    return get_product_by_id_and_slug(id, slug)