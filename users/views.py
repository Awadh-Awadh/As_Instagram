from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
          #saving user
            post = form.save(commit=False)
            post.save()

            username = form.cleaned_data.get('username')
            #flush message
            messages.success(request, f'account creation for {username}')
            #account already created. Redirect user to a different route
            return redirect('login')

    else:
        form = RegistrationForm()
      
    
    return render(request,'users/register.html',{'form':form})