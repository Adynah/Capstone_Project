from rest_framework import permissions

class IsOwnerOrStaff(permissions.BasePermission):
    """
    Custom permission:
    - Customers can access only their own bookings
    - Staff/Admin can access all bookings
    """

    def has_object_permission(self, request, view, obj):
        # Staff/Admin have full access
        if request.user.role in ['admin', 'staff']:
            return True
        
        # Only owner can access
        return obj.customer == request.user
    