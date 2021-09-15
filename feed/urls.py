from django.urls import path
from . import views


urlpatterns = [
  path('',views.feed, name='feed'),
  path('dm/',views.dms, name = 'dm'),
  path('profile/',views.profile, name = 'profile'),
  path('edit/',views.edit, name = 'edit'),
  path('post/',views.post, name = 'post')
  ]