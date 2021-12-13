from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_bookings, name="all_bookings"),
    path('create/', views.create, name="create_booking"),
    path('edit/', views.edit, name="edit_booking"),
    path('delete/', views.delete, name="delete_booking"),
]