from django.urls import path
from .views import BookingCreateView, BookingListView

urlpatterns = [
    path('book/', BookingCreateView.as_view(), name='booking/create'),
    path('bookings/', BookingListView.as_view(), name='bookings/list'),
]
