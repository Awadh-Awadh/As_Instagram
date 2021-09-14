from django.urls import path
from . import views


urlpatterns = [
  path('feed/',views.feed, name='feed'),
  path('dm/',views.dms, name = 'dm'),
  path('profile/',views.profile, name = 'profile'),
  path('edit/',views.edit, name = 'edit')
  ]