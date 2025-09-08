from django.db import models
from accounts.models import User

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    )
    delivery_name = models.CharField(max_length=255)   # Recipient name
    delivery_phone = models.CharField(max_length=20)   # Recipient phone

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    pickup_address = models.TextField()
    delivery_address = models.TextField()
    estimated_time = models.DurationField(max_length=100)
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking {self.id} for {self.customer.username}"
