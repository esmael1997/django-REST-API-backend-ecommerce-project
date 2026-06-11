from django.urls import path
from accounts.api.views import PasswordResetRequestAPIView, PasswordResetConfirmAPIView

urlpatterns = [
    path("password-reset/", PasswordResetRequestAPIView.as_view()),
    path("password-reset/confirm/", PasswordResetConfirmAPIView.as_view()),
]