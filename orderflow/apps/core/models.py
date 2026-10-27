from django.db import models
import uuid

# Create your models here.

class Basemodel(models.Model) :
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract =True
    
class Adress(Basemodel):
    street = models.CharField(max_length=255,blank=True)
    city = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    postal_code = models.CharField(max_length=10,blank=True)
    country = models.CharField(max_length=100,blank=True)
    is_default = models.BooleanField(default=True)
    