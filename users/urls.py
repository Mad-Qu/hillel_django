from django.urls import path
from .views import users, SignUpView

app_name = "users"

urlpatterns = [
    path("", users),
    path("signup/", SignUpView.as_view(), name="signup"),
]
