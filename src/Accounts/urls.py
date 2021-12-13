from django.urls import path
from . import views
import Bookings.views


urlpatterns = [
    path('create/', views.create, name="create"),
    path('<str:username>/', views.account, name="account"),
    path('<str:username>/book-game/', Bookings.views.create, name="create_booking"),
    path('<str:username>/delete/', views.delete, name="delete"),
    path('<str:username>/edit/', views.edit, name="edit")
]