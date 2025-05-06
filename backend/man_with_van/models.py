from django.db import models

# Create your models here.

class ShippingOrder(models.Model):
    # Sender fields
    sender_lat = models.FloatField()
    sender_lon = models.FloatField()
    sender_address_text = models.TextField()
    sender_name = models.CharField(max_length=255)
    sender_phone = models.CharField(max_length=20)
    sender_post_code = models.CharField(max_length=20)
    pickup_from_time = models.DateTimeField()
    pickup_to_time = models.DateTimeField()

    # Recipient fields
    recipient_lat = models.FloatField()
    recipient_lon = models.FloatField()
    recipient_address_text = models.TextField()
    recipient_name = models.CharField(max_length=255)
    recipient_phone = models.CharField(max_length=20)
    recipient_post_code = models.CharField(max_length=20)
    delivery_from_time = models.DateTimeField()
    delivery_to_time = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order from {self.sender_name} to {self.recipient_name}"
