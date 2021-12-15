from django.shortcuts import render, redirect
from django.http import Http404
from .models import Booking
from .forms import NewBookingForm

# Create your views here.


def view_bookings( request, **kwargs  ):
    """
    view bookings page when the user is logged in
    """
    user = request.user

    # if 'id' in kwargs:
    #     _id = kwargs.pop( 'id' )

    #     match user.is_authenticated:
    #         case 1:
    #             pass

    if 'id' in kwargs and user.is_authenticated:
        _id = kwargs.pop( 'id' )
        if _id != user.UserID:
            raise Http404( 'You dont have access to this page. I should use a different code but I dont know how; that is why this is a 404' )

        data = { 'booking_entries': Booking.objects.filter( CustomerID = _id ) }
        return render( request, 'viewbookings.html', data )

    elif 'id' in kwargs and not user.is_authenticated:
        raise Http404( 'You dont have access to this page. I should use a different code but I dont know how; that is why this is a 404' )

    elif 'id' not in kwargs and user.is_authenticated:
        return redirect('view_user_bookings', user.UserID)

    else:
        return render( request, 'viewbookings.html', {} )



def create(request):
    """
    create new bookings
    """
    if request.method == 'POST':
        form = NewBookingForm(request.POST)
        if form.is_valid():
            return redirect('view_bookings')

    else:
        form = NewBookingForm()

    return render(request, 'bookingform.html', {'createform': form})


def edit(request):
    pass


def delete(request):
    pass
