from django.urls import path
from .views import *
from .views import ProfileView
from apps.accounts import views
from .import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView
#app_name = 'accounts'

urlpatterns = [
    #path('accounts/', include('django.contrib.auth.urls')),
    path("password-reset/",auth_views.PasswordResetView.as_view(template_name="apps/accounts/password_reset.html"),name="password_reset",),
    path("password-reset/done/",auth_views.PasswordResetDoneView.as_view(template_name="apps/accounts/password_reset_done.html"),name="password_reset_done",),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="apps/accounts/password_reset_confirm.html"),name="password_reset_confirm",),
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name="apps/accounts/password_reset_complete.html"),name="password_reset_complete",),
    path("", views.IndexView.as_view(), name="index"),
    path('register/',register_view,name='register'),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("password-reset/",CustomPasswordResetView.as_view(),name="password_reset",)
]
