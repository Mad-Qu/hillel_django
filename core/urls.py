from django.urls import path
from .views import posts

app_name = "core"

urlpatterns = [path("", posts)]
