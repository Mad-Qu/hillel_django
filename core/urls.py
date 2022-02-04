from django.urls import path
from .views import PostView, PostDetailView, PostDeleteView


app_name = "posts"

urlpatterns = [
    path("", PostView.as_view(), name="list"),
    path("<int:post_id>/", PostDetailView.as_view(), name="detail"),
    path("<int:post_id>/delete", PostDeleteView.as_view(), name="delete"),
]
