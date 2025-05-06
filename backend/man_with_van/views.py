from django.shortcuts import render
from rest_framework import viewsets
from .models import ShippingOrder
from .serializers import ShippingOrderSerializer

# Create your views here.

class ShippingOrderViewSet(viewsets.ModelViewSet):
    queryset = ShippingOrder.objects.all()
    serializer_class = ShippingOrderSerializer
