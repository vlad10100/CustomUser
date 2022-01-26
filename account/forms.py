from django.forms import Form

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'birthday',
            'password1',
            'password2'
        ]

