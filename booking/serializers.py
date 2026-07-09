from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id', 'email', 'vehicle', 'pickup_date', 'dropoff_date', 
            'unit_price', 'promo_code', 'payment_method', 'total_cost', 'status', 'created_at'
        ]

