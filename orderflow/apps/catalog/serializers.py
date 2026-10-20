from orderflow.apps.catalog.models import Product,Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name")
        
class PorductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta :
         model =Product
         fields = "__all__"
         read_only_fields =("id","created_at","updated_at")
         