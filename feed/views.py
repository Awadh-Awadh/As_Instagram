from django.shortcuts import redirect, render
from .models import Image,Profile,User,Comments
from .forms import UpdateProfile, UpdateUser,Post
# Create your views here.


def feed(request):
    image = Image.objects.all()
    context = {
      'posts':image
    }
    return render(request, 'feed/feed.html', context)

def dms(request):
    return render(request, 'feed/dms.html')

def profile(request):
    logged_in_user = request.user
    posts = Image.objects.filter(user=logged_in_user).count()
    images = Image.objects.filter(user=logged_in_user).all()
    context = {
      'posts':posts,
      'images': images
    }

    
    return render(request, 'feed/profile.html',context)

def edit(request):
    if request.method == 'POST':
         u_form = UpdateUser(request.POST, instance =request.user)
         p_form = UpdateProfile(request.POST, request.FILES, instance = request.user.profile)
         if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UpdateUser(instance=request.user)
        p_form = UpdateProfile(instance=request.user.profile)
    context = {
      'u_form':u_form,
      'p_form':p_form

    }
    return render(request, 'feed/pedit.html',context)

def post(request):
  if request.method == 'POST':
      form = Post(request.POST,request.Files)
      if form.is_valid():
          form.save()
          return redirect('feed')
      else:
          post_form = Post()
          context = {
              'form':post_form
            }

  return render(request, 'feed/post.html',context)