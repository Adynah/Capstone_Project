from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'customer', 'pickup_address', 'delivery_address', 'estimated_time', 'estimated_cost', 'status', 'date_created']
        read_only_fields = ['customer', 'status', 'date_created']
    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1")
        return value
    
    def validate_estimated_time(self, value):
        if value <= 0:
            raise serializers.ValidationError("Estimated time must be positive")
        return value

    def validate_estimated_cost(self, value):
        if value <= 0:
            raise serializers.ValidationError("Estimated cost must be positive")
        return value
    
    def create(self, validated_data):
        validated_data['customer'] = self.context['request'].user
        return super().create(validated_data)
