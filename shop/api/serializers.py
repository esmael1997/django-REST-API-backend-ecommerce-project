from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(read_only=True,slug_field="slug")

    class Meta:
        model = Product
        fields = ["id","title","slug","price","description",]