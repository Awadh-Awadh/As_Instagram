from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import registrationForm

# Create your views here.
def register(request):
    form = registrationForm()
    context = {
      'form':form
    }
    return render(request, 'users/register.html', context)