from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from shop.models import Product
from cart.models import Cart
from cart.api.v1.serializers import CartSerializer
from cart.services import add_item , remove_item, get_or_create_cart

class CartViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        cart = get_or_create_cart(request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    
    @action(detail=False, methods=["post"])
    def add_item(self, request):
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))

        product = Product.objects.get(id=product_id)

        item = add_item(
            user=request.user,
            product=product,
            quantity=quantity
        )

        return Response({
            "message": "Item added successfully",
            "item_id": item.id
        })
        
    @action(detail=False, methods=["post"])
    def remove_item(self, request):
        product_id = request.data.get("product_id")

        product = Product.objects.get(id=product_id)

        remove_item(
            user=request.user,
            product=product
        )

        return Response({"message": "Item removed"})
    
    @action(detail=False, methods=["post"])
    def clear(self, request):
        cart = get_or_create_cart(request.user)
        cart.items.all().delete()

        return Response({"message": "Cart cleared"})