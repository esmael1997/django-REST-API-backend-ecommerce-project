from rest_framework.routers import DefaultRouter
from shop.api.v1.views import ProductViewSet

router = DefaultRouter()
router.register("products", ProductViewSet, basename="products")

urlpatterns = router.urls
