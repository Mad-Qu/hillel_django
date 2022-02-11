from django.urls import path
from .views import PostView, PostDetailView, PostDeleteView, PostCreateView, PostUpdateView


app_name = "posts"

urlpatterns = [
    path("", PostView.as_view(), name="list"),
    path("<int:post_id>/", PostDetailView.as_view(), name="detail"),
    path("<int:post_id>/delete", PostDeleteView.as_view(), name="delete"),
    path("post_update/<int:post_id>/", PostUpdateView.as_view(), name="update"),
    path("post_create/", PostCreateView.as_view(), name="create")
]
