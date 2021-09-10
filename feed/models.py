from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.fields.files import ImageField

# Create your models here.
class Image(models.Model):
    image = ImageField(upload_to = 'images/')
    name = CharField(max_length=200)
    caption = TextField()
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    likes = IntegerField()
    comments = TextField()



    def __str__(self):
        return self.name
