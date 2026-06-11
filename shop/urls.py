from django.urls import path
from shop.api.v1 import views

app_name = "shop"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("category/<slug:slug>/",views.product_list_by_category,name="product_list_by_category",),
    path("<int:id>/<slug:slug>/", views.product_detail, name="product_detail"),
]
