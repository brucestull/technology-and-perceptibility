# from django import  forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Import our CustomUser model from 'users.models.py'.
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Specifies the CustomUser for use in user creation form.
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    """
    Specifies the CustomUser for use in user change form.
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
