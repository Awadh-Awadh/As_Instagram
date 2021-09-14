from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE

# Create your models here.
class Image(models.Model):
    image = CloudinaryField('images')
    name = models.CharField(max_length=200)
    caption = models.TextField()
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    likes = models.ManyToManyField("Likes")
    comments = models.ForeignKey("Comments", on_delete=CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pp = CloudinaryField('images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Comments(models.Model):
    comment = models.CharField(max_length= 300)
    def __str__(self):
        return self.comment

class Likes(models.Model):
    likes = models.IntegerField()

    def __str__(self):
        return self.likes