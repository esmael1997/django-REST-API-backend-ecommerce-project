from django.urls import path
from apps.contact.api.v1.views import ContactMessageAPIView

urlpatterns = [
    path("contact/", ContactMessageAPIView.as_view(), name="contact"),
]