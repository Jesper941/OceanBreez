
# bookings forms
from django import forms
from .models import Booking
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, User


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date', 'time']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
