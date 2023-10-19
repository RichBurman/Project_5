from django.shortcuts import render
from allauth.account.views import SignupView
from .forms import CustomUserRegistrationForm

# Create your views here.


class CustomUserRegistrationView(SignupView):
    form_class = CustomUserRegistrationForm
