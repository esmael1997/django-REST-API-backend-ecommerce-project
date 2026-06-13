from django.db import transaction
from cart.models import Cart, CartItem
from cart.exceptions import (
    ProductNotAvailableException,
    InsufficientStockException,
    CartItemNotFoundException,
)


def get_or_create_cart(user):
    return Cart.objects.get_or_create(user=user)[0]

@transaction.atomic
def add_item(user, product, quantity=1):
    if not product.is_available():
        raise ProductNotAvailableException()

    if quantity <= 0:
        return None

    cart = get_or_create_cart(user)

    item, created = CartItem.objects.select_related("product").get_or_create(
        cart=cart,
        product=product,
        defaults={"quantity": quantity},
    )

    if not created:
        new_quantity = item.quantity + quantity

        if new_quantity > product.stock:
            raise InsufficientStockException()

        item.quantity = new_quantity
        item.save(update_fields=["quantity"])

    return item

@transaction.atomic
def update_item_quantity(user, item_id, quantity):
    cart = get_or_create_cart(user)

    try:
        item = CartItem.objects.select_related("product").get(
            id=item_id,
            cart=cart,
        )
    except CartItem.DoesNotExist:
        raise CartItemNotFoundException()

    if quantity <= 0:
        item.delete()
        return None

    if quantity > item.product.stock:
        raise InsufficientStockException()

    item.quantity = quantity
    item.save(update_fields=["quantity"])

    return item

@transaction.atomic
def remove_item(user, item_id):
    cart = get_or_create_cart(user)

    try:
        item = CartItem.objects.get(
            id=item_id,
            cart=cart,
        )
    except CartItem.DoesNotExist:
        raise CartItemNotFoundException()

    item.delete()
    
@transaction.atomic
def clear_cart(user):
    cart = get_or_create_cart(user)
    cart.items.all().delete()
    
    


    
    
