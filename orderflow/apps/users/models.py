from django.db import models
from django.contrib.auth.models import AbstractUser
from orderflow.apps.core.models import Adress

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=15,blank=True)
    email = models.EmailField(max_length=255,unique=True)
    adress = models.ForeignKey(Adress,blank=True,null=True,on_delete=models.SET_NULL,related_name ="user_adress")
    
    
    
