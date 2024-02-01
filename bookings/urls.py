from django.urls import path
from django.contrib.auth.views import LoginView
from .views import book_table, booking_success, index, menu, contact, booking

urlpatterns = [
    path('book-table/', book_table, name='book_table'),
    path('booking-success/', booking_success, name='booking_success'),
    path('index/', index, name='index'),
    path('menu/', menu, name='menu'),
    path('contact/', contact, name='contact'),
    path('booking/', booking, name='booking'),
    path('login/', LoginView.as_view(template_name='booking.html'), name='login'),
]
