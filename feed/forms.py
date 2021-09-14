from django import forms
from .models import Profile,User

class UpdateProfile(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','username']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','pp']