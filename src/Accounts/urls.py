from django.urls import path
from . import views
import Bookings.views


urlpatterns = [
    path('create/', views.create, name="create_account"),
    path('login/', views.login, name="login_account"),
    path('<str:id>/', views.account, name="view_account"),
    path('<str:id>/delete/', views.delete, name="delete"),
    path('<str:id>/edit/', views.edit, name="edit")
]