from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("booking/", views.booking, name="booking"),
    path("account/", views.account, name="account"),
    path("test/", views.test, name="test"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("create-account/", views.register, name="register_account_form"),
]