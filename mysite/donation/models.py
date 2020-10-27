from django.db import models

# Create your models here.

class Donation(models.Model):
    name = models.CharField(max_length= 1000 , blank=True)
    amount = models.CharField(max_length=100 , blank=True)
    email = models.EmailField(max_length=255)
    order_id = models.CharField(max_length=1000 )
    paid = models.BooleanField(default=False)
