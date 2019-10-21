from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from product.models import Product 
# Create your models here.


class CustomerUser(AbstractUser):
    address =models.CharField(max_length=300,default='')
    phone_number=models.CharField(max_length=15,default='')