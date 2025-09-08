from rest_framework import generics, permissions, viewsets
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.response import Response
from .permissions import IsOwnerOrStaff

class BookingViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Booking.
    
    Features:
    - Customers can perform CRUD on their own bookings
    - Staff/Admin can perform CRUD on all bookings
    - Filtering by `status` and `date_created` query params
    - Bookings are sorted by `date_created` descending
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrStaff]

    def get_queryset(self):
        user = self.request.user
        qs = Booking.objects.all() if user.role in ['admin', 'staff'] else Booking.objects.filter(customer=user)

        # Filtering
        status_param = self.request.query_params.get('status')
        date_param = self.request.query_params.get('date')

        if status_param:
            qs = qs.filter(status=status_param)
        if date_param:
            qs = qs.filter(date_created__date=date_param)

        # Sorting by date_created descending
        return qs.order_by('-date_created')

    # Booking request
    def perform_create(self, serializer):
        # Automatically assign current user as the customer
        serializer.save(customer=self.request.user)

    # Update booking
    def perform_update(self, serializer):
        serializer.save()

    # Delete booking
    def destroy(self, request, *args, **kwargs):
        booking = self.get_object()
        self.check_object_permissions(request, booking)  # Enforce IsOwnerOrStaff
        booking.delete()
        return Response({"message": "Booking deleted successfully"}, status=status.HTTP_200_OK)
    