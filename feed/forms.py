from django import forms
from .models import Profile,User, Image

class UpdateUser(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','pp']

class Post(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        exclude = ('user',)