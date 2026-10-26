from django.db import models
from orderflow.apps.core.models import Basemodel
from orderflow.apps.users.models import User
from orderflow.apps.catalog.models import Product

# Create your models here.
class Order(Basemodel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="order_users")
    status = models.CharField(max_length=20,default="PENDING")
    total = models.DecimalField(max_digits=10,blank=True,decimal_places=2)
    
class OrderItem(Basemodel):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="order_items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="order_product")
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(blank=True, max_digits=5, decimal_places=2)
    
class IdempotencyKey(Basemodel):
    key = models.CharField(max_length=255,blank= True)
    request_hash = models.TextField(blank= True)
    response = models.TextField(blank= True)
    
    
class OutboxEvent(Basemodel):
    event_type = models.CharField(max_length=20,blank= True)
    payload = models.JSONField(blank=True,null=True)
    published_at = models.DateTimeField(blank=True,null=True)
    
    