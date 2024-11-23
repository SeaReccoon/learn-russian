from django.views.generic import DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse

def getCurrentAccount(request):
    if not request.user:
        return reverse('index')
    return reverse("account", args=[request.user.pk,])

class LoginAccountView(LoginView):
    template_name = "user/login.html"

    def get_success_url(self):
        return getCurrentAccount(self.request)

class RegistrationView(CreateView):
    model = User
    template_name = "user/registration.html"
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse("login")

class AccountView(DetailView):
    model = User
    template_name = "user/account.html"
    context_object_name = 'user'
