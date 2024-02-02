from django.urls import path
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from .views import book_table, booking_success, index, menu, contact, booking, register, change_booking, edit_booking

# All necessary urlpatterns
urlpatterns = [
    path('index/', index, name='index'),
    path('menu/', menu, name='menu'),
    path('contact/', contact, name='contact'),
    path('booking/', booking, name='booking'),
    path('book-table/', book_table, name='book_table'),
    path('booking-success/', booking_success, name='booking_success'),
    path('change-booking/', change_booking, name='change_booking'),
    path('bookings/edit-booking/<int:booking_id>/', edit_booking, name='edit_booking'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
