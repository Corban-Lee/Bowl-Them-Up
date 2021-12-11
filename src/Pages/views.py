from django.shortcuts import render

# Create your views here.

def index_view(request):
    print(request.user)
    return render(request, "index.html", {})


def contact_view(request):
    return render(request, "contact.html", {})


def booking_view(request):
    return render(request, "booking.html", {})


def register_view(request):
    return render(request, "register.html", {})


def login_view(request):
    return render(request, "login.html", {})