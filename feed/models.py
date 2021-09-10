from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length=200)
    caption = models.TextField()
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    likes = models.IntegerField()
    comments = models.TextField()



    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pp = models.ImageField(upload_to = 'images/')
    bio = TextField()

    def __str__(self):
        return self.user.username