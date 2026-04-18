from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email", "avatar", "telephone", "country", "password1", "password2")
