from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


def users(request):
    users = User.objects.all()
    results = ", ".join([user.username for user in users])
    return HttpResponse(results)


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"