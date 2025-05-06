from django.contrib import admin
from .models import ShippingOrder

@admin.register(ShippingOrder)
class ShippingOrderAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'recipient_name', 'pickup_from_time', 'delivery_from_time')
    search_fields = ('sender_name', 'recipient_name', 'sender_phone', 'recipient_phone')
    list_filter = ('created_at', 'updated_at')
