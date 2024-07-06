from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'barber'),
        (3, 'customer'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

class Service(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()  # Duration in minutes

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer = models.ForeignKey(CustomUser, related_name='bookings', on_delete=models.CASCADE)
    barber = models.ForeignKey(CustomUser, related_name='appointments', on_delete=models.CASCADE)
    service = models.ForeignKey(Service, related_name='bookings', on_delete=models.CASCADE)
    time_slot = models.DateTimeField()
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f'{self.customer} - {self.service} - {self.time_slot}'
