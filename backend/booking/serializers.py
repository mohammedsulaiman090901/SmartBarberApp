from rest_framework import serializers
from .models import CustomUser, Service, Booking, Barber

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'user_type')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'duration')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'service', 'user', 'start_time', 'end_time')

class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = ('id', 'user', 'rating')
