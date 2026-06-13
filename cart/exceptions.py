class CartException(Exception):
    """Base cart exception."""
    pass


class ProductNotAvailableException(CartException):
    """Product is not available."""
    pass


class InsufficientStockException(CartException):
    """Requested quantity exceeds available stock."""
    pass


class CartItemNotFoundException(CartException):
    """Cart item does not exist."""
    pass