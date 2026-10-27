from django.shortcuts import render
# Create your views here.
from rest_framework import permissions
from orderflow.apps.orders.models import Order,OrderItem
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import UpdateModelMixin
from rest_framework.exceptions import ValidationError
from orderflow.apps.orders.serializers import OrderSerializer,OrderItemSerializer,OrderUpdateSerializer


class OrderViewset(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer
    http_method_names = ["get", "post","patch","delete"]
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    

class OrderItemViewset(GenericViewSet,UpdateModelMixin):
    serializer_class = OrderUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return OrderItem.objects.filter(order__user=self.request.user)
