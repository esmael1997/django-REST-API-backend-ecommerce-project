
from rest_framework.viewsets import ReadOnlyModelViewSet
from shop.api.serializers import ProductSerializer
from shop.api.pagination import ProductPagination
from shop.services.product_service import list_products 


class ProductViewSet(ReadOnlyModelViewSet):
    
    pagination_class = ProductPagination 
    serializer_class = ProductSerializer

    def get_queryset(self):
        return list_products()