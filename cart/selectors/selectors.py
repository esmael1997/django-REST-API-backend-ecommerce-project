from cart.models import Cart
from decimal import Decimal

def get_cart(user):
    return Cart.objects.select_related("user").prefetch_related(
        "items__product"
    ).get(user=user)
    
def calculate_totals(cart):
    subtotal = Decimal("0")

    for item in cart.items.all():
        subtotal += item.total_price

    discount = Decimal("0")
    tax = Decimal("0")

    total = subtotal - discount + tax

    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "total": total,
    }
    
