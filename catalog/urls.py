from django.urls import path
from .views import AdminLoginView, summarize_book_view, generate_tags_view
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("admin/login", AdminLoginView.as_view()),
    path("admin/refresh", TokenRefreshView.as_view()),
    path("summarize-book/", summarize_book_view, name="summarize-book"),
    path("generate-tags/", generate_tags_view, name="generate-tags"),
]
