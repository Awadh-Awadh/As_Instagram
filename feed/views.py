from django.shortcuts import render
from .models import Image,Profile,User,Comments
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
    print(posts)
    context = {
      'posts':posts
    }

    
    return render(request, 'feed/profile.html',context)

def edit(request):
    return render(request, 'feed/pedit.html')