from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BarberDashboardView,
    RegisterUser,
    ServiceListCreateView,
    BookingListCreateView,
    BookingDetailView,
    CustomerDashboardView,
    ShowSecretKey,
    ServiceViewSet,
    BarberListView
)

router = DefaultRouter()
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('barber-dashboard/', BarberDashboardView.as_view(), name='barber-dashboard'),
    path('customer-dashboard/', CustomerDashboardView.as_view(), name='customer-dashboard'),
    path('services/', ServiceListCreateView.as_view(), name='service-list-create'),
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking-detail'),
    path('show-secret-key/', ShowSecretKey.as_view(), name='show_secret_key'),
    path('barbers/', BarberListView.as_view(), name='barber-list'),
]

# Add the router URLs to the urlpatterns
urlpatterns += router.urls
