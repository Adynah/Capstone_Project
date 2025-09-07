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
        user = self.request.user
        if user.role in ['admin', 'staff']:
            qs = Booking.objects.all()
        else:
            qs = Booking.objects.filter(customer=user)
        
        # Filtering
        status = self.request.query_params.get('status')
        date = self.request.query_params.get('date')  # expects YYYY-MM-DD

        if status:
            qs = qs.filter(status=status)
        if date:
            qs = qs.filter(date_created__date=date)

        # Sorting by date_created descending
        qs = qs.order_by('-date_created')

        return qs

# API to update booking status
class BookingStatusUpdateView(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role in ['admin', 'staff']:
            return Booking.objects.all()
        return Booking.objects.none()
    