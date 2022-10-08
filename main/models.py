from datetime import datetime
from email import message
from secrets import choice
from django.db import models

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

LIFESTYLE_CHOICES = (
        ('Healthy', 'Healthy'),
        ('Corporate', 'Corporate'),
        ('City', 'City'),
        ('Rural', 'Rural'),
        ('Nomadic', 'Nomadic'),
    )

ACTIVITY_CHOICES = (
        ('N', 'No exercise'),
        ('O', 'Occasional, light exercise'),
        ('R', 'Regular exercise and training'),
        ('D', 'Daily training'),
    )

FREQUENCY_CHOICES = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

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
    gender = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    lifestyle = models.CharField(max_length=100)
    activity_level = models.CharField(max_length=100)
    goal = models.CharField(max_length=250,blank=True)
    frequency = models.CharField(max_length=100)

    def __str__(self):
        return self.name