from django.shortcuts import render, redirect
from django.http import Http404
from .models import Booking

# Create your views here.


def view_bookings( request, **kwargs  ):
    """
    view bookings page when the user is logged in
    """
    if '_id' in kwargs and request.user.is_authenticated:
        data = { 'booking_entries': Booking.object.filter( CustomerID = _id ) }
        return render( request, 'viewbookings.html', data )

    elif '_id' in kwargs and not request.user.is_authenticated:
        raise Http404( 'You dont have access to this page. I should use a different code but I dont know how; that is why this is a 404' )

    elif 'id' not in kwargs and request.user.is_authenticated:
        return redirect('view_user_bookings')
        #
        #  redirect url bookings/<int:id>/ if they 
        #

    else:
        return render( request, 'viewbookings.html', {} )



def create(request):
    return render(request, 'createbooking.html', {})


def edit(request):
    pass


def delete(request):
    pass
