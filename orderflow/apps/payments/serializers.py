from orderflow.apps.payments.models import Payment
from rest_framework import serializers

class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"