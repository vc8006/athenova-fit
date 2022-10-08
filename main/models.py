from datetime import datetime
from email import message
from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to='myimage')
    date = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=250,blank=True)
    message = models.TextField(blank=True)
    date = models.DateField(blank=True,default=datetime.now())

    def __str__(self):
        return self.name