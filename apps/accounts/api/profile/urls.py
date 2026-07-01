from django.urls import path
from apps.accounts.api.profile.views import ProfileAPIView, ChangePasswordAPIView


urlpatterns = [
    path("", ProfileAPIView.as_view(), name="profile"),
    path("", ChangePasswordAPIView.as_view(), name="change-password"),
    
]