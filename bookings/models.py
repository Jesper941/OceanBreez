from django import forms
from django.db import models
from django.contrib.auth.models import User


# Booking model class
class Booking(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateField()
    time = models.TimeField()
    company_size = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.name} - {self.date} {self.time}'

# Changing your booking class
class ChangeBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_to_change = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.booking_to_change.name}'