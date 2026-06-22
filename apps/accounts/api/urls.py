from django.urls import path
from apps.accounts.api.views import PasswordResetRequestAPIView, PasswordResetConfirmAPIView,RegisterAPIView, LoginAPIView

urlpatterns = [
    path("password-reset/", PasswordResetRequestAPIView.as_view()),
    path("password-reset/confirm/", PasswordResetConfirmAPIView.as_view()),
    path("register/", RegisterAPIView.as_view()),
    path("login/", LoginAPIView.as_view()),
]