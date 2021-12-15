from django.urls import path
from . import views


urlpatterns = [
    #     path          function                    call-name
    path('',         views.view_bookings, name="view_bookings"      ),
    path('<int:id>', views.view_bookings, name="view_user_bookings" ),
    path('create/',  views.create,        name="create_booking"     ),
    path('edit/',    views.edit,          name="edit_booking"       ),
    path('delete/',  views.delete,        name="delete_booking"     ),
]