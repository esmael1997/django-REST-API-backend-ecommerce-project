from django.urls import path
from accounts.api.views import PasswordResetRequestAPIView

urlpatterns = [
    path("password-reset/", PasswordResetRequestAPIView.as_view()),
]