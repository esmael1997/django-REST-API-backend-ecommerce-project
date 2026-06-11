from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True, slug_field="slug")
    is_available = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "slug",
            "price",
            "description",
            "image",
            "stock",
            "category",
            "is_available",
        ]

    def get_is_available(self, obj):
        return obj.is_available()