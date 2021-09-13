from django.shortcuts import render
from .models import Image
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
  return render(request, 'feed/profile.html')