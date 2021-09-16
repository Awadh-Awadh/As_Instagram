from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save


# Create your models here.
class Image(models.Model):
    image = CloudinaryField('images')
    name = models.CharField(max_length=200)
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-pk']


    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.OneToOneField(Image, on_delete=models.CASCADE)
    pp = CloudinaryField('images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Comments(models.Model):
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    comment_name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField()

    def comment_save(self):
        self.save()
    class Meta:
        verbose_name = 'comment'
    
    def __str__(self):
        return self.comment_name.username


# def user_profile(sender,**kwargs):
#     if kwargs['created']:
#         prof = Profile.objects.create(user=kwargs['instance'])

# post_save.connect(user_profile, sender=User)