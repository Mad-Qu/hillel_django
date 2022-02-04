from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include
from django.urls.base import reverse_lazy



urlpatterns = [
    path("", lambda x: HttpResponseRedirect(reverse_lazy("posts:list"))),
    path("admin/", admin.site.urls),
    path("posts/", include("core.urls")),
    # path("users/", include("users.urls")),
]
