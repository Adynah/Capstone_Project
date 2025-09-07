from django.urls import path
from .views import BookingCreateView, BookingListView, BookingStatusUpdateView

urlpatterns = [
    path('book/', BookingCreateView.as_view(), name='booking/create'),
    path('bookings/', BookingListView.as_view(), name='bookings/list'),
    path('bookings/<int:pk>/status/', BookingStatusUpdateView.as_view(), name='booking/status-update'), 
]
