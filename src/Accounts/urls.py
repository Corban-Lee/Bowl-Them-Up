from django.urls import path
from . import views
import Bookings.views


urlpatterns = [
    path('create/', views.register, name="create_account"),
    path('signout/', views.signoutPage, name="signout_account"),
    path('login/', views.loginPage, name="login_account"),
    # path('<str:id>/', views.account, name="view_account"),
    # path('<str:id>/delete/', views.delete, name="delete"),
    # path('<str:id>/edit/', views.edit, name="edit")
]