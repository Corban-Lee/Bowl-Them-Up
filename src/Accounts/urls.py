from django.urls import path
from . import views
import Bookings.views


urlpatterns = [
    path('create/', views.create, name="create_account"),
    path('login/', views.login, name="login_account"),
    path('<str:username>/', views.account, name="view_account"),
    path('<str:username>/delete/', views.delete, name="delete"),
    path('<str:username>/edit/', views.edit, name="edit")
]