# bookings/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm, ChangeBookingForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Booking


def booking(request):
    login_form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('book_table')
        else:
            # Handle invalid login
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'booking.html', {'login_form': login_form})

@login_required
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Associate the booking with the logged-in user
            booking.save()
            return redirect('booking_success') 
    else:
        form = BookingForm()

    return render(request, 'bookings/book_table.html', {'form': form})


@login_required
def booking_success(request):
    return render(request, 'bookings/booking_success.html')

@login_required
def change_booking(request):
    if request.method == 'POST':
        form = ChangeBookingForm(request.user, request.POST)
        if form.is_valid():
            booking_to_change = form.cleaned_data['booking_to_change']
            return redirect('edit_booking', booking_id=booking_to_change.id)

    form = ChangeBookingForm(request.user)
    return render(request, 'bookings/change_booking.html', {'change_booking_form': form})

@login_required
def edit_booking(request, booking_id):
    existing_booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=existing_booking)
        if form.is_valid():
            form.save()
            return redirect('edit_booking', booking_id=existing_booking.id)

    form = BookingForm(instance=existing_booking)
    return render(request, 'bookings/edit_booking.html', {'form': form})




def register(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_table')
    return render(request, 'registration.html', {'form': form})


def home_view(request):
    return render(request, 'index.html', {'variable': 'value'})

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    flashed_messages = [message.message for message in get_messages(request)]
    return render(request, 'contact.html', {'flashed_messages': flashed_messages})

def message_success(request):
    messages.success(request, 'Your message was sent successfully!')
    return redirect('contact_page')
