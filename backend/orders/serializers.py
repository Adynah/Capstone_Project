from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'customer', 'pickup_address', 'delivery_address', 'estimated_time', 'estimated_cost', 'status', 'date_created']
        read_only_fields = ['customer', 'status', 'date_created']
    
    # Validate quantity
    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1")
        return value
    
    # Validate estimated time
    def validate_estimated_time(self, value):
        if value <= 0:
            raise serializers.ValidationError("Estimated time must be positive")
        return value

    # Validate estimated cost
    def validate_estimated_cost(self, value):
        if value <= 0:
            raise serializers.ValidationError("Estimated cost must be positive")
        return value
    
    # Validate date 
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
    
