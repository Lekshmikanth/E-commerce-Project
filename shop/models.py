from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=150, null=False,blank=False)
    image=models.ImageField(upload_to="getfilename",null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    createdat=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    def getfilename(request,filename):
        now_time=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        newfilename="%s%s"%(now_time,filename)
        return os.path.join('uploads/',newfilename)

class Product(models.Model):
    category=models.ForeignKey("category",on_delete=models.CASCADE)
    name=models.CharField(max_length=150, null=False,blank=False)
    product_image=models.ImageField(upload_to="getfilename",null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=1000,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    createdat=models.DateTimeField(auto_now_add=True)
    trending=models.BooleanField(default=False,help_text="0-default,1-trending")
    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    @property
    def total_cost(self):
        return self.product_qty*self.product.price
    
class Favourite(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)