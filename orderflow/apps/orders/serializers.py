from rest_framework import serializers
from orderflow.apps.orders.models import Order,OrderItem
from orderflow.apps.catalog.models import Product 
from rest_framework.serializers import ValidationError



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model =  OrderItem
        fields = "__all__"
        read_only_fields = ("id","created_at","updated_at","unit_price")
        
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
        order = Order.objects.create(user=self.context["request"].user,**validated_data)
        total = 0
        for item in item_data:
            product = item["product"]
            quantity = item["quantity"]
            unit_price = product.price
            OrderItem.objects.create(
                order =order,
                product = product,
                quantity = quantity,
                unit_price =unit_price ,
            )
            total += quantity * unit_price
        order.total = total
        order.save()
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
          raise ValidationError("The Pending Order cannot be modified") 
        return attrs
    def update(self, instance, validated_data):
        instance =  super().update(instance, validated_data)
        order =instance.order
        total =sum((item.quantity * item.unit_price for item in order.order_items.all()),start=0)
        order.total = total
        order.save(update_fields=["total"])
        return instance
        
    
      
    
            
            