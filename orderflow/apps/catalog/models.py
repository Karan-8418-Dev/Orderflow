from django.db import models
from orderflow.apps.core.models import Basemodel

# Create your models here.
class Category(Basemodel):
    name = models.CharField(max_length=100,unique=True)
    
    
class Product(Basemodel):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name="products")
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        indexes = [models.Index(fields=("category","is_active"))]
    