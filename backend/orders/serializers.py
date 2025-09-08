from rest_framework import serializers
from .models import Booking
from datetime import timedelta

ALLOWED_STATUSES = ['pending', 'completed', 'in transit', 'delivered', 'cancelled']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [ 'id', 'order_id', 'delivery_name', 'delivery_phone', 'pickup_address', 'delivery_address', 'estimated_time', 'estimated_cost', 'status', 'date_created']
        read_only_fields = ['customer', 'id', 'order_id', 'status', 'date_created']
    
    # Ensure status is valid
    def validate_status(self, value):
        if value not in ALLOWED_STATUSES:
            raise serializers.ValidationError(f"Status must be one of {ALLOWED_STATUSES}.")
        return value
    
    # Validate estimated time
    def validate_estimated_time(self, value):
        if not isinstance(value, timedelta):
            raise serializers.ValidationError("Estimated time must be a valid duration (HH:MM:SS).")
        if value.total_seconds() <= 0:
            raise serializers.ValidationError("Estimated time must be greater than zero.")
        return value

    # Validate estimated cost
    def validate_estimated_cost(self, value):
        if value <= 0:
            raise serializers.ValidationError("Estimated cost must be positive")
        return value
    
    # Validate data 
    def create(self, validated_data):
        validated_data['customer'] = self.context['request'].user
        return super().create(validated_data)
    
    # Validate that addresses are provided
    def validate_pickup_address(self, value):
        if not value.strip():
            raise serializers.ValidationError("Pickup address cannot be empty.")
        return value
    
    # Validate that addresses are provided
    def validate(self, data):
        if data['pickup_address'] == data['delivery_address']:
            raise serializers.ValidationError("Pickup and delivery addresses cannot be the same.")
        return data
    
