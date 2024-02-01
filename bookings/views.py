# bookings/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import BookingForm, RegistrationForm


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
            booking.user = request.user
            booking.save()
            return redirect('booking_success') 
    else:
        form = BookingForm()

    return render(request, 'bookings/book_table.html', {'form': form})

@login_required
def booking_success(request):
    return render(request, 'bookings/booking_success.html')

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
