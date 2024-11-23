from django.views.generic import DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse

class LoginAccountView(LoginView):
    template_name = "user/login.html"

    def get_success_url(self):
        return reverse("account", args=[self.request.user.pk,])

class RegistrationView(CreateView):
    model = User
    template_name = "user/registration.html"

class AccountView(DetailView):
    model = User
    template_name = "user/account.html"
    context_object_name = 'user'
