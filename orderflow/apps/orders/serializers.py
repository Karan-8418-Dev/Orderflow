from rest_framework import serializers
from orderflow.apps.orders.models import Order,OrderItem
from orderflow.apps.catalog.models import Product 
from rest_framework.serializers import ValidationError
from django.db import transaction
from django.db.models import F
from orderflow.apps.catalog.serializers import PorductSerializer
from orderflow.apps.users.serializers import UserRelatedSerializer



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model =  OrderItem
        fields = "__all__"
        read_only_fields = ("id","created_at","updated_at","unit_price","order")
        
class OrderItemDetailSerializer(serializers.ModelSerializer):
    product = PorductSerializer(read_only=True,required = False)
    class Meta:
        model = OrderItem
        fields =("id","product","quantity","unit_price","created_at")
    

class OrderDetailSerializer(serializers.ModelSerializer):
    order_items = OrderItemDetailSerializer(read_only=True,required = False)
    user = UserRelatedSerializer(read_only=True,required = False)
    class Meta:
        model:Order
        fields = ("id","order_items","status","total","billing_adress","shipping_adress","user")
    
        
class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many =True,required=True)
    class Meta:
        model = Order
        fields= "__all__"
        read_only_fields = ("id","user","status","total","created_at","updated_at")
        
    def validate(self, attrs):
        if not attrs["order_items"]:
            raise ValidationError({"Details":"At Least one order item is required "})
            
        return attrs
    def create(self, validated_data):
        item_data = validated_data.pop("order_items")
        user = self.context["request"].user
        with transaction.atomic():
        
            order = Order.objects.create(user=self.context["request"].user,**validated_data)
            total = 0
            for item in item_data:
                product_instance = item["product"]
                quantity = item["quantity"] 
                product = Product.objects.select_for_update().get(id=product_instance.id)
                if product.stock < quantity:
                    raise ValidationError({"details":f"Insufficient stock for '{product.name}',Available '{product.stock},Request ]"})
                Product.objects.filter(id=product.id).update(stock = F("stock")-quantity)
                OrderItem.objects.create(
                    order =order,
                    product = product,
                    quantity = quantity,
                    unit_price =product.price ,
                )
                total += quantity * product.price
            order.total = total
            order.save(update_fields=["total"])
            return order
        
class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields =("id","quantity")
        
    def validate_quantity(self,value):
        if value<1:
            raise ValidationError("At Least one item should be kept")
        return value
        
    def validate(self, attrs):
        if self.instance.order.status != "PENDING":
          raise ValidationError("Only Pending Order can be modified") 
        return attrs
    def update(self, instance, validated_data):
        instance =  super().update(instance, validated_data)
        order =instance.order
        total =sum((item.quantity * item.unit_price for item in order.order_items.all()),start=0)
        order.total = total
        order.save(update_fields=["total"])
        return instance
        
    
      
    
            
            