from django.urls import include, path
from apps.accounts.api.profile.urls import ProfileAPIView,ChangePasswordAPIView
from apps.accounts.api.auth.urls import(
    LoginAPIView,
    LogoutAPIView,
    CurrentUserAPIView,
    RegisterAPIView,
    PasswordResetConfirmAPIView,
    PasswordResetRequestAPIView,
    
    ) 

urlpatterns = [
    path("profile/", ProfileAPIView.as_view()),
    path("change-password/", ChangePasswordAPIView.as_view()),
    path("Login/", LoginAPIView.as_view()),
    path("Logout/", LogoutAPIView.as_view()),
    path("CurrentUser/", CurrentUserAPIView.as_view()),
    path("Register/", RegisterAPIView.as_view()),
    path("PasswordResetConfirm/", PasswordResetConfirmAPIView.as_view()),
    path("PasswordResetRequest/", PasswordResetRequestAPIView.as_view()),
    
]
