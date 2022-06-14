from pyexpat import model
from django.db import models
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class Customuser(AbstractUser):
    # username = None
    email = models.EmailField(max_length=50,unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Product(models.Model):
    barcode_number = models.IntegerField()
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Category(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_code = models.IntegerField()
    packs_per_carton = models.IntegerField()
    

class Inventory(models.Model):
    product = models.ForeignKey(Category,on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Transaction(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    prod_code = models.IntegerField()
    barcode = models.IntegerField()
    no_of_cartons = models.IntegerField()
    barcode_img = models.ImageField('images',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
        
    def save(self,*args,**kwargs):
        pr=barcode.get_barcode_class('EAN13')
        Ean = pr(f"{self.barcode}345",ImageWriter())
        buffer = BytesIO()
        Ean.write(buffer)
        self.barcode_img.save(f"{self.prod_code}.png",File(buffer),save=False)
        return super().save(*args,**kwargs)
