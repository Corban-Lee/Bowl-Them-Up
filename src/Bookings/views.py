from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .models import BookingModel, LaneModel
from .forms import BookingForm



def view_bookings( request, **kw  ):
    """view bookings page when the user is logged in"""

    # Get user object
    User = request.user

    # Try to show the users bookings
    if 'id' in kw and User.is_authenticated:
        _id = kw.pop( 'id' )
        # prevent users from looking at other users bookings
        if _id != User.UserID:
            raise PermissionDenied()
        # return render of webpage with booking info
        return render(request, 'viewbookings.html', {'booking_entries': BookingModel.objects.filter( Customer = User )})


    # Prevent user from looking at bookings without being logged-in
    elif 'id' in kw and not User.is_authenticated:
        raise PermissionDenied()


    # Redirect user to same view but via different url that shows their ID  (maybe unecessary. could just show bookings in this func if user is auth'd)
    elif 'id' not in kw and User.is_authenticated:
        return redirect('view_user_bookings', User.UserID)

    # Show the bookings page with no booking data
    else:
        return render( request, 'viewbookings.html', {} )



def create(request):
    """create new bookings"""

    # Render page with new form if the method is not post
    if request.method != 'POST':
        form = BookingForm()
        return render(request, 'bookingform.html', { 'form':form })

    form = BookingForm(request.POST)

    if form.is_valid():
        # Save without commiting to database
        form.save(commit=False)

        # Set the form customer to the currently logged-in user
        form.instance.Customer = request.user

        # Set the form lane to a random available lane
        Lane = LaneModel.objects.order_by('Available')[0]
        Lane.Available = False
        Lane.save()
        form.instance.Lane  = Lane

        # Commit to database
        form.save()

        # Redirect user to show them their bookings including this one they have
        # just created.
        return redirect('view_bookings')
        
        
    return render(request, 'bookingform.html', { 'form':form })



def edit(request):
    pass



def delete(request, id):
    """Delete a booking from the database"""

    Booking = BookingModel.objects.filter(Id=id)
    Lane = Booking.values('Lane')
    Lane.Available = True
    Lane.update()
    Booking.delete()
    print('deleted booking')
    return redirect('view_bookings')
