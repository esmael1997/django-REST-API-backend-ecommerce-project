from django.urls import path
from apps.newsletter.api.v1.views import NewsletterSubscribeAPIView

urlpatterns = [
    path("newsletter/subscribe/", NewsletterSubscribeAPIView.as_view()),
]