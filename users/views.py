from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import registrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = registrationForm()
    context = {
        'form':form
      }
    return render(request, 'users/register.html', context)