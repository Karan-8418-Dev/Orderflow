from django.shortcuts import render
from rest_framework import permissions,viewsets
from orderflow.apps.catalog.serializers import CategorySerializer,PorductSerializer
from orderflow.apps.catalog.models import Product,Category
# Create your views here.

class Categoryviewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class Productviewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = PorductSerializer
    permission_classes= [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ["category","is_active"]
    search_fields = ["name"]
    
    
        


