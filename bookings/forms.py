
# bookings/forms.py
from django import forms
from .models import Booking  # Assuming you have a model named Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time']
