from django.urls import path
from .views import book_table, booking_success, index, menu, contact, booking

urlpatterns = [
    path('book-table/', book_table, name='book_table'),
    path('booking-success/', booking_success, name='booking_success'),
    path('index/', index, name='index'),
    path('menu/', menu, name='menu'),
    path('contact/', contact, name='contact'),
    path('booking/', booking, name='booking'),
]
