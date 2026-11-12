from django.shortcuts import render
# Create your views here.
from rest_framework import permissions
from orderflow.apps.orders.models import Order,OrderItem
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import UpdateModelMixin
from rest_framework.exceptions import ValidationError
from orderflow.apps.orders.serializers import OrderSerializer,OrderItemSerializer,OrderUpdateSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.db.models import F
from orderflow.apps.catalog.models import Product
from orderflow.apps.orders.serializers import OrderItemDetailSerializer

class OrderViewset(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "post","patch","delete"]
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related("order_items__product").select_related("billing_adress","shipping_adress","user")
    
    def  get_serializer_class(self):
        if self.action in ["list","retrieve"]:
            return OrderItemDetailSerializer
        return OrderSerializer

    @action(detail=True,methods=["POST"],url_path ="cancel")
    def cancel(self,request,pk=None):
        order =self.get_object()
        
        if order.status != "PENDING":
            return Response({"error":f"Cannot cancel order with '{order.status}' status"},status=status.HTTP_400_BAD_REQUEST)
        
        with transaction.atomic():
            for item in order.order_items.all():
                Product.objects.filter(id = item.product_id).update(stock =F("stock")+ item.quantity)
            order.status = "CANCELLED"
            order.save(update_fields =["status"])
            
        return Response({"message":"Products Cancelled Successfuly","status":order.status},status=status.HTTP_202_ACCEPTED)
            
    

class OrderItemViewset(GenericViewSet,UpdateModelMixin):
    serializer_class = OrderUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return OrderItem.objects.filter(order__user=self.request.user)
            