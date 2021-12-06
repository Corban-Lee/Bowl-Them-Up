from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "views/index.html")

def contact(request):
    return render(request, "views/contact.html")

def booking(request):
    return render(request, "views/booking.html")

def account(request):
    return render(request, "views/account.html")

def test(request):
    return render(request, "views/test.html")
    
def register(request):
    return render(request, "views/register.html")
