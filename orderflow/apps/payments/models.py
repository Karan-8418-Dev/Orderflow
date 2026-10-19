from django.db import models
from orderflow.apps.core.models import Basemodel
from orderflow.apps.orders.models import Order

# Create your models here.
class Payment(Basemodel):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="payment_order")
    amount = models.DecimalField(max_digits=10)
    status = models.CharField(max_length=15,default="PENDING")
    provider_ref = models.CharField(max_length=155,blank=True,null=True)
    