from allauth.account.forms import SignupForm
from .models import CustomUser


class CustomUserRegistrationForm(SignupForm):
    class Meta:
        model = CustomUser
