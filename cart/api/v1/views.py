from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from shop.api.v1.core.base import BaseAPIViewMixin

from cart.api.v1.serializers import (
    CartSerializer,
    AddCartItemSerializer,
    UpdateCartItemSerializer,
)

from cart.services.services import (
    add_item,
    update_item_quantity,
    remove_item,
    clear_cart,
)

from cart.selectors.selectors import get_cart

from shop.models import Product

class CartViewSet(BaseAPIViewMixin, ViewSet):
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        cart = get_cart(request.user)

        serializer = CartSerializer(cart)

        return self.success(
            data=serializer.data
        )
        
    def create(self, request):
        serializer = AddCartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = Product.objects.get(
            id=serializer.validated_data["product_id"]
        )

        item = add_item(
            user=request.user,
            product=product,
            quantity=serializer.validated_data["quantity"],
        )

        return self.success(
            data={
                "item_id": item.id if item else None
            },
            code=status.HTTP_201_CREATED
        )
        
    def partial_update(self, request, pk=None):
        serializer = UpdateCartItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        item = update_item_quantity(
            user=request.user,
            item_id=pk,
            quantity=serializer.validated_data["quantity"],
        )

        return self.success(
            data={
                "item_id": item.id if item else None,
                "quantity": item.quantity if item else 0,
            }
        )
        
    def destroy(self, request, pk=None):
        remove_item(
            user=request.user,
            item_id=pk,
        )

        return self.success(
            data={
                "message": "Item removed"
            }
        )
        
    @action(detail=False, methods=["delete"])
    def clear(self, request):
        clear_cart(request.user)

        return self.success(
            data={
                "message": "Cart cleared"
            }
        )
        
