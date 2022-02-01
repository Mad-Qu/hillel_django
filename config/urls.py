from cgitb import html
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("posts/", include("core.urls")),
    path("users/", include("users.urls")),
]
