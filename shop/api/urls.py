from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop.api.views import ProductViewSet

app_name = "Shop_api"

router = DefaultRouter()

router.register(
    r"products",
    ProductViewSet,
    basename="products"
)

urlpatterns = [
    path("", include(router.urls)),
]