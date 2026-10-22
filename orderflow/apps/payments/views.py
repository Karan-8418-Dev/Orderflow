from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ReadOnlyModelViewSet
from orderflow.apps.payments.models import Payment
from rest_framework import permissions
from orderflow.apps.payments.serializers import PaymentHistorySerializer


class PaymentHistoryViewset(ReadOnlyModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentHistorySerializer
    permission_classes=[permissions.IsAuthenticated]