from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ReadOnlyModelViewSet
from shop.api.serializers import ProductSerializer
from shop.api.pagination import ProductPagination
from shop.api.filters import ProductFilter
from shop.models import Product
from shop.selectors.product_selector import get_products


class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter,]

    filterset_class = ProductFilter

    search_fields = ["title", "description"]
    ordering_fields = ["price", "created_at", "title"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return Product.objects.filter(available=True)
    