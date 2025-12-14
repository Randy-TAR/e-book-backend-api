from django.urls import path
from .views import AdminLoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("admin/login", AdminLoginView.as_view()),
    path("admin/refresh", TokenRefreshView.as_view()),
]
