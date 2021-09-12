from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Image(models.Model):
    image = CloudinaryField('images')
    name = models.CharField(max_length=200)
    caption = models.TextField()
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    likes = models.IntegerField()
    comments = models.TextField()



    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pp = CloudinaryField('images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username