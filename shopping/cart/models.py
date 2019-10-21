from django.db import models
from product.models import Product
from user.models import CustomerUser
# Create your models here.


class Cart(models.Model):
    user=models.ForeignKey(CustomerUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    products=models.ManyToManyField(Product)
class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    
