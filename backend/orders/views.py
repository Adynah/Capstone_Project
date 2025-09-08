from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from .models import Booking
from .serializers import BookingSerializer
from .permissions import IsOwnerOrStaff

class BookingViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Booking.
    Customers can perform CRUD on their own bookings.
    Staff and admin can perform CRUD on all bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrStaff]

    def get_queryset(self):
        user = self.request.user
        # Base queryset: all for staff/admin, own bookings for customer
        qs = Booking.objects.all() if user.role in ['admin', 'staff'] else Booking.objects.filter(customer=user)

        # Filtering
        status_param = self.request.query_params.get('status')
        date_param = self.request.query_params.get('date')

        if status_param:
            qs = qs.filter(status=status_param)
        
        if date_param:
            try:
                date_obj = parse_date(date_param)
                if date_obj:
                    qs = qs.filter(date_created__date=date_obj)
                else:
                    # Ignore invalid date format
                    pass
            except Exception:
                # Optionally log the error
                pass

        # Sorting by newest first
        return qs.order_by('-date_created')

    def perform_create(self, serializer):
        try:
            serializer.save(customer=self.request.user)
        except Exception as e:
            raise serializers.ValidationError({"error": f"Failed to create booking: {str(e)}"})

    def perform_update(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            raise serializers.ValidationError({"error": f"Failed to update booking: {str(e)}"})

    def destroy(self, request, *args, **kwargs):
        try:
            booking = self.get_object()
            self.check_object_permissions(request, booking)  # enforce IsOwnerOrStaff
            booking.delete()
            return Response({"message": "Booking deleted successfully"}, status=status.HTTP_200_OK)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"Failed to delete booking: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
   