from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

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
    
class RootView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # List bookings (GET)
    def get(self, request):
        user = request.user
        if user.role in ['admin', 'staff']:
            bookings = Booking.objects.all()
        else:
            bookings = Booking.objects.filter(customer=user)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create booking (POST)
    def post(self, request):
        serializer = BookingSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update booking (PUT/PATCH)
    def put(self, request, booking_id=None):
        try:
            booking = Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookingSerializer(booking, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete booking (DELETE)
    def delete(self, request, booking_id=None):
        try:
            booking = Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)
        
        booking.delete()
        return Response({"message": "Booking deleted successfully"}, status=status.HTTP_200_OK)
    