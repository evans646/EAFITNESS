from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField

class FitnessPlan(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    summary = models.TextField(default='')
    image = models.ImageField(upload_to ='uploads/',default=True)
    premium = models.BooleanField(default=True)

    def __str__(self):
           return self.title

           
class Customer(models.Model):
    user = OneToOneField(User,on_delete=models.CASCADE)
    stripeid = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
    cancel_at_period_end  = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)
    
    

   

