from django.urls import path, re_path
from . import views



urlpatterns = [
    path('', views.view_bookings, name="view_bookings"), # show the booking page to the user
    path('<int:id>', views.view_bookings, name="view_user_bookings"), # show the user their bookings (if logged in)
    path('create/', views.create, name="create_booking"), # create a booking
    path('edit/', views.edit, name="edit_booking"), # edit a booking
    path('delete/<int:id>/',  views.delete, name="delete_booking"), # delete a booking
]