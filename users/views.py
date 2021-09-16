from django.shortcuts import render,redirect
# from .forms import RegistrationForm
from django.contrib import messages


def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password1=request.POST['password']
    password2 = request.POST['password2']
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
          #saving user
            post = form.save(commit=False)
            post.image_id = request.user.id
            form.save()

            username = form.cleaned_data.get('username')
            #flush message
            messages.success(request, f'account creation for {username}')
            #account already created. Redirect user to a different route
            return redirect('login')

    else:
        form = RegistrationForm()
      
    
    return render(request,'users/register.html',{'form':form})


