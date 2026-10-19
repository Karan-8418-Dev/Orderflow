from django.db import models
from orderflow.apps.core.models import Basemodel

# Create your models here.

class FAQDocument(Basemodel):
    text = models.TextField(blank=True)
    
class Embedding(Basemodel):
    document = models.ForeignKey(FAQDocument,on_delete=models.CASCADE,null=True,related_name="embedding")
    vector = models.JSONField()