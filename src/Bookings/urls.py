from django.urls import path
from . import views


urlpatterns = [
    path('', views.confirm_loggedin, name="confirm_loggedin"),
]