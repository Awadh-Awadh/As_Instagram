from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class registrationForm(UserCreationForm):
    class Meta:
        model = User
        field = ['username', 'email','password1','password2']