from django.urls import path
from .views import PostView

app_name = "core"

urlpatterns = [
    path("", PostView.as_view()),
]
