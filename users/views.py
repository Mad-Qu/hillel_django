from django.views import generic
from .forms import SignUpForm
from django.urls import reverse_lazy


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')