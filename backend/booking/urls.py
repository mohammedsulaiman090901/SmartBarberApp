from django.urls import path
from .views import BarberDashboardView, RegisterUser

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('barber-dashboard/', BarberDashboardView.as_view(), name='barber-dashboard'),
]
