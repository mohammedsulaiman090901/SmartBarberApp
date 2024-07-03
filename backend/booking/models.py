from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'customer'),
        (2, 'barber'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)

class Booking(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='customer_bookings')
    barber = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='barber_bookings')
    time_slot = models.DateTimeField()
    status = models.CharField(max_length=50, default='pending')

class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()  # duration in minutes
