from django.shortcuts import render
# Create your views here.
from rest_framework import permissions
from orderflow.apps.orders.models import Order,OrderItem
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.exceptions import ValidationError
from orderflow.apps.orders.serializers import OrderSerializer,OrderItemSerializer,OrderUpdateSerializer


class OrderViewset(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer
    http_method_names = ["get", "post","patch","delete"]
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    

class OrderItemViewset(ReadOnlyModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get"]
    
    def get_queryset(self):
        return OrderItem.objects.filter(order__user=self.request.user)
    
    def get_serializer_class(self):
        if self.action == "partial_update":
            return OrderUpdateSerializer
        return OrderUpdateSerializer
    
