from django.db import models
from orderflow.apps.core.models import Basemodel
from django.utils.text import slugify

# Create your models here.
class Category(Basemodel):
    name = models.CharField(max_length=100,unique=True)
    
    
class Product(Basemodel):
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name="products")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    sku = models.CharField(max_length=20,blank=True)
    attachment = models.ImageField(upload_to="products/",blank=True)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    slug = models.CharField(max_length=200,blank=True)
    
    
    class Meta:
        indexes = [models.Index(fields=("category","is_active"))]
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save( *args, **kwargs)