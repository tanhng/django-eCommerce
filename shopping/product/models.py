from django.db import models


# Create your models here.


class Category(models.Model):
    title=models.CharField(max_length=200,default='')
    description=models.TextField(default='')
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.title
class Product(models.Model):
    title = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    image=models.FileField(null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    price=models.IntegerField(default=0)
    def __str__(self):
        return self.title
