from django.urls import path
from apps.accounts.api.auth.views import PasswordResetRequestAPIView, PasswordResetConfirmAPIView,RegisterAPIView, LoginAPIView, LogoutAPIView,CurrentUserAPIView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("password-reset/",PasswordResetRequestAPIView.as_view()),
    path("password-reset-confirm/",PasswordResetConfirmAPIView.as_view(), name="password-reset-confirm"),
    path("register/",RegisterAPIView.as_view()),
    path("login/",LoginAPIView.as_view()),
    path("refresh/",TokenRefreshView.as_view(),name="token_refresh",),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    #path("me/", CurrentUserAPIView.as_view(), name="current-user"),
   
]
