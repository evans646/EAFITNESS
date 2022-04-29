from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from cloudinary.models import CloudinaryField

class FitnessPlan(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    summary = models.TextField(default='')
    image = CloudinaryField('image')
    premium = models.BooleanField(default=True)

    def __str__(self):
           return self.title

class FitnessBlog(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    summary = models.TextField(default='')
    image = CloudinaryField('image')
    premium = models.BooleanField(default=True)

    def __str__(self):
           return self.title
           
class Customer(models.Model):
    user = OneToOneField(User,on_delete=models.CASCADE)
    stripeid = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
    cancel_at_period_end  = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)
           
class Food(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    text = models.TextField(default='')
    image = CloudinaryField('image')
    date = models.DateTimeField()
    premium = models.BooleanField(default=True)

    def __str__(self):
           return self.name
           
class Health(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    text = models.TextField(default='')
    date = models.DateTimeField()
    image = CloudinaryField('image')
    premium = models.BooleanField(default=True)

    def __str__(self):
           return self.title
           
           
class Love(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    text = models.TextField(default='')
    date = models.DateTimeField()
    image = CloudinaryField('image')
    premium = models.BooleanField(default=True)

    def __str__(self):
           return self.title
           
           
class Beauty(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    text = models.TextField(default='')
    date = models.DateTimeField()
    image = CloudinaryField('image')
    premium = models.BooleanField(default=True)

    def __str__(self):
           return self.title
           
class Culture(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    text = models.TextField(default='')
    date = models.DateTimeField()
    image = CloudinaryField('image')
    premium = models.BooleanField(default=True)

    def __str__(self):
           return self.title
           
