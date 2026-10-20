from rest_framework import serializers
from orderflow.apps.users.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,min_length = 8)
    class Meta:
        model= User
        fields=("id","username","email","phone","password")
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta : 
        model = User
        fields = "__all__"
        