from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer

# API to create a booking
class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # automatically assign the logged-in user as customer
        serializer.save(customer=self.request.user)

# API to list bookings for the logged-in user
class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(customer=self.request.user)
