
# bookings forms
from django import forms
from .models import Booking, ChangeBooking
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, User


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time','company_size']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ChangeBookingForm(forms.ModelForm):
    class Meta:
        model = ChangeBooking
        fields = ['booking_to_change']

    def __init__(self, user, *args, **kwargs):
        super(ChangeBookingForm, self).__init__(*args, **kwargs)
        self.fields['booking_to_change'].queryset = Booking.objects.filter(user=user)