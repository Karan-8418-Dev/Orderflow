from django.shortcuts import render

# Create your views here.
from rest_framework import permissions,generics
from orderflow.apps.users.serializers import UserSerializer,UserRegistrationSerializer

class Registerview(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes  = [permissions.AllowAny]
    
class Profileview(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user

    
    