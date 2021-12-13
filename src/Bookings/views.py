from django.shortcuts import render
from .models import Booking

# Create your views here.


def all_bookings(request):

    data = Booking.objects.all()
    booking = {
        'all_bookings': data
    }

    return render(request, 'viewbookings.html', booking)

def create(request):
    return render(request, 'createbooking.html', {})


def edit(request):
    pass


def delete(request):
    pass
