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
    duration = models.DurationField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.service.name} - {self.user.username}"

class Barber(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    rating = models.FloatField()

    def __str__(self):
        return self.user.username
