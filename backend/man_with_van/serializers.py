from rest_framework import serializers
from .models import ShippingOrder

class ShippingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingOrder
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at') 