# bookings/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

@login_required
def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')  # create a success page
    else:
        form = BookingForm()

    return render(request, 'bookings/book_table.html', {'form': form})

    def booking_success(request):
        return render(request, 'bookings/booking_success.html')
    