from django.contrib import admin
from django.urls import path, include

from core.models import Post
from core.views import posts


urlpatterns = [
    path("admin/", admin.site.urls),
    path("posts/", include("core.urls")),
]
