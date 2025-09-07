from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'customer', 'pickup_address', 'delivery_address', 'estimated_time', 'estimated_cost', 'status', 'date_created']
        read_only_fields = ['customer', 'status', 'date_created']
