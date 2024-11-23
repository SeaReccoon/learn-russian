from django.urls import path
from user.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('account/<int:pk>', AccountView.as_view(), name="account"),
    path('registration/', RegistrationView.as_view(), name="registration"),
    path('login/', LoginAccountView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout')
]