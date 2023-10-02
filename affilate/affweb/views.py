from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import SignUpForm, SignInForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class SignInView(LoginView):
    form_class = SignInForm
    template_name = 'registration/login.html'
