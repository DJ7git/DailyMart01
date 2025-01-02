from django.db import models

# Create your models here.

class Category(models.Model): 
   categoryname = models.CharField(max_length=30)
   categoryimage = models.ImageField(upload_to='images/')

class Product(models.Model):
   productname = models.CharField(max_length=30)
   productimage = models.ImageField(upload_to='images/')
   productprice = models.FloatField()
   productcategory = models.CharField(max_length=30)
   productdescription = models.TextField()