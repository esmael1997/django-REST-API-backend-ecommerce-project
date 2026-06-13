from rest_framework import serializers
from cart.models import Cart, CartItem
from cart.selectors.selectors import calculate_totals

class CartItemSerializer(serializers.ModelSerializer):

    product_id = serializers.UUIDField(
        source="product.id",
        read_only=True,
    )

    title = serializers.CharField(
        source="product.title",
        read_only=True,
    )

    price = serializers.DecimalField(
        source="product.price",
        read_only=True,
        max_digits=12,
        decimal_places=2,
    )

    total_price = serializers.ReadOnlyField()

    class Meta:
        model = CartItem

        fields = (
            "id",
            "product_id",
            "title",
            "price",
            "quantity",
            "total_price",
        )
        
        
class CartSerializer(serializers.ModelSerializer):

    items = CartItemSerializer(
        many=True,
        read_only=True,
    )

    totals = serializers.SerializerMethodField()

    class Meta:
        model = Cart

        fields = (
            "id",
            "items",
            "totals",
        )

    def get_totals(self, obj):
        return calculate_totals(obj)


class AddCartItemSerializer(serializers.Serializer):
    product_id = serializers.UUIDField()
    quantity = serializers.IntegerField(min_value=1)
    
class UpdateCartItemSerializer(serializers.Serializer):
    quantity = serializers.IntegerField(min_value=1)