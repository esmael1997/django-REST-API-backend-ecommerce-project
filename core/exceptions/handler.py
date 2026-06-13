from rest_framework.views import exception_handler
from rest_framework import status

from shop.api.v1.core.response import APIResponse

from cart.exceptions import (
    ProductNotAvailableException,
    InsufficientStockException,
    CartItemNotFoundException,
)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # DRF handled exceptions (ValidationError, NotFound, etc.)
    if response is not None:
        return APIResponse.error(
            message="Request failed",
            errors=response.data,
            code=response.status_code
        )
        
    if isinstance(exc, ProductNotAvailableException):
        return APIResponse.error(
            message="Product is not available",
            code=status.HTTP_400_BAD_REQUEST
        )

    if isinstance(exc, InsufficientStockException):
        return APIResponse.error(
            message="Not enough stock available",
            code=status.HTTP_400_BAD_REQUEST
        )

    if isinstance(exc, CartItemNotFoundException):
        return APIResponse.error(
            message="Cart item not found",
            code=status.HTTP_404_NOT_FOUND
        )
        
    return APIResponse.error(
        message="Internal server error",
        code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
    
