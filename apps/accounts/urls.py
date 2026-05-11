from django.urls import path
from .views import *
from .views import profile_view
from apps.accounts import views
from .import views

app_name = 'accounts'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('register/',register_view,name='register'),
    path("profile/", profile_view, name="profile"),
]
