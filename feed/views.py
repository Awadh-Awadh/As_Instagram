from django.shortcuts import redirect, render
from .models import Image,Profile,User,Comments
from .forms import UpdateProfile, UpdateUser,Post
from django.contrib.auth.decorators import login_required
# Create your views here.
     

@login_required
def feed(request):
    image = Image.objects.all()
    comments = Comments.objects.all()
    context = {
      'posts':image,
      'comments':comments
    }
    return render(request, 'feed/feed.html', context)
@login_required
def dms(request):
    return render(request, 'feed/dms.html')
@login_required
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
        form = Post(request.POST,request.FILES)
        if form.is_valid():
            obj= form.save(commit = False)
            obj.user = request.user
            form.save()
            return redirect('feed')
    else:
        form = Post()
        context = {
                  'form':form
              }

    return render(request, 'feed/post.html',context)

def comment(request):
  query = request.POST.get('comment')
  if query:
      comment = Comments.objects.create(comment_body = query)
      comment.save()
      return redirect(feed)