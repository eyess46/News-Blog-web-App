from django.db import models
from datetime import datetime

# Create your models here.

class News(models.Model):
    story_title = models.CharField(max_length=255)
    story_body = models.CharField(max_length=5000000)
    category = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    storydate_posted = models.DateTimeField(default=datetime.now, blank=True)


class Sport(models.Model):
    story_title = models.CharField(max_length=255)
    story_body = models.CharField(max_length=5000000)
    category = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    storydate_posted = models.DateTimeField(default=datetime.now, blank=True)

class Politics(models.Model):
    story_title = models.CharField(max_length=255)
    story_body = models.CharField(max_length=5000000)
    category = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    storydate_posted = models.DateTimeField(default=datetime.now, blank=True) 


class Business(models.Model):
    story_title = models.CharField(max_length=255)
    story_body = models.CharField(max_length=5000000)
    category = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    storydate_posted = models.DateTimeField(default=datetime.now, blank=True)

    
class Contactform(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField(unique= True)
    subject = models.CharField(max_length= 100)
    message = models.CharField(max_length= 900)
