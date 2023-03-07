from datetime import date
from django.db import models
from django.utils import timezone



# Create your models here.
class Product(models.Model):
    label = models.CharField(max_length=20, default='')
    price = models.FloatField(default=0)
    stock = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='image/product_image',null=True, blank=True )
    description = models.TextField(null=True, blank=True)
    expirationDate = models.DateField(default=date(2023,12,31))
    fabricationDate = models.DateField(default=date.today)

class Client(models.Model):
    firstName = models.CharField(max_length=50, default='')
    lastName = models.CharField(max_length=50, default='')
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, default='+21600000000')
    birthdate = models.DateField(default=date(1995,11,11))
    typeClient = models.CharField(max_length=50, choices=[('LOYAL','Loyal Customer'),
    ('Normall','Normal Customer'),('VIP',' Vip Customer')], default='Normal')
    # Relationship:
    clientProduct = models.ManyToManyField(Product, through='Command', through_fields=('client', 'product'))

class Command(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE) # utiliser en relation 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # utiliser en relation 
    date = models.DateField(default=timezone.now())
    quality = models.PositiveSmallIntegerField(default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
