from django.shortcuts import render
from rest_framework import permissions,viewsets
from orderflow.apps.catalog.serializers import CategorySerializer,PorductSerializer
from orderflow.apps.catalog.models import Product,Category
from orderflow.apps.core.permissions import IsAdminOrReadOnly
# Create your views here.

class Categoryviewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    
    
class Productviewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = PorductSerializer
    permission_classes= [IsAdminOrReadOnly]
    filterset_fields = ["category","is_active"]
    search_fields = ["name"]
    
    
        


