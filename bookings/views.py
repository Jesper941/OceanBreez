# bookings/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import get_messages


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


def home_view(request):
    return render(request, 'index.html', {'variable': 'value'})

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    flashed_messages = [message.message for message in get_messages(request)]
    return render(request, 'contact.html', {'flashed_messages': flashed_messages})

def booking (request):
    return render(request, 'booking.html')

def message_success(request):
    messages.success(request, 'Your message was sent successfully!')
    return redirect('contact_page')
