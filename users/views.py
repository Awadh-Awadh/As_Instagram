from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# Create your views here.
def register(request):
    form = UserChangeForm()
    context = {
      'form':form
    }
    return render(request, 'users/register.html', context)