from rest_framework.viewsets import ReadOnlyModelViewSet
from shop.api.v1.serializers import ProductSerializer
from shop.api.v1.pagination import ProductPagination
from shop.api.v1.core.base import BaseAPIViewMixin
#from shop.services.product_service import list_products


class ProductViewSet(BaseAPIViewMixin, ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        serializer = self.get_serializer(page, many=True)

        return self.success(
            data=serializer.data,
            meta={
                "count": queryset.count()
            }
        )

    def get_queryset(self):
        pass
        #return list_products(self.request.query_params)