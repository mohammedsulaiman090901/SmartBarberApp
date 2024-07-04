from django.urls import path
from .views import BarberDashboardView, RegisterUser, ServiceListCreateView, BookingListCreateView, BookingDetailView, CustomerDashboardView, ShowSecretKey

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('barber-dashboard/', BarberDashboardView.as_view(), name='barber-dashboard'),
    path('customer-dashboard/', CustomerDashboardView.as_view(), name='customer-dashboard'),
    path('services/', ServiceListCreateView.as_view(), name='service-list-create'),
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('show-secret-key/', ShowSecretKey.as_view(), name='show_secret_key'),
]
