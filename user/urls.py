from django.urls import path
from .views import CustomUserRegistrationView

urlpatterns = [
    path('signup/', CustomUserRegistrationView.as_view(), name='custom_signup'),
]