from shop.models import Product


def get_available_products():
    return Product.objects.filter(available=True)


def get_product_by_id_and_slug(id, slug):
    return Product.objects.get(id=id, slug=slug, available=True)