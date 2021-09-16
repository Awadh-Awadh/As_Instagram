from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField()
#     firstname= forms.CharField(max_length=200)
#     lastname = forms.CharField(max_length=200)
#     class Meta:
#         model = User
#         fields = ['username', 'firstname','lastname','email','password1','password2']
#         exclude = []