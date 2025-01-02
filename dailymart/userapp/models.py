from django.db import models
from adminapp.models import *

# Create your models here.

class userdata(models.Model):
   dbusername = models.CharField(max_length=30)
   dbuserpassword = models.CharField(max_length=30)
   dbusermail = models.EmailField(max_length=254)
   dbuserphone = models.IntegerField()

class feedbackdata(models.Model):
   feedbackuser = models.CharField(max_length=30)
   feedbackmail = models.EmailField(max_length=30)
   feedbackreview = models.CharField(max_length=500)

class Cart(models.Model):
   usercart = models.ForeignKey(userdata,on_delete=models.CASCADE)
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity = models.IntegerField()
   total = models.FloatField()
   status = models.IntegerField(default=0)

class Checkout(models.Model):
   usercheckout = models.ForeignKey(userdata,on_delete=models.CASCADE)
   usercart = models.ForeignKey(Cart,on_delete=models.CASCADE)
   address = models.CharField(max_length=200)
   city = models.CharField(max_length=20)
   pincode = models.IntegerField()
   country = models.CharField(max_length=20)