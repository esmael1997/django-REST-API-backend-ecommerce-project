from rest_framework.routers import DefaultRouter
from django.urls import path, include
from shop.api.v1.views import ProductViewSet

router = DefaultRouter()
router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
]