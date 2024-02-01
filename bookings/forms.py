
# bookings forms
from django import forms
from .models import Booking
from django.contrib.auth.forms import AuthenticationForm


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time']
