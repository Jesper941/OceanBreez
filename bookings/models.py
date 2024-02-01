from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateField()
    time = models.TimeField()
    pass

    def __str__(self):
        return f'{self.name} - {self.date} {self.time}'
