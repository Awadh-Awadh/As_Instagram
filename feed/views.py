from django.shortcuts import render

# Create your views here.


def feed(request):
    p = "it works"
    context = {
      'p':p 
    }
    return render(request, 'feed/feed.html',context)