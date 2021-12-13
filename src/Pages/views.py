from django.shortcuts import render

# Create your views here.

def index_view(request):
    print(request.user)
    return render(request, "index.html", {})


def contact_view(request):
    return render(request, "contact.html", {})


def create_booking(request):
    if request.method == "POST":
        print("First Name:", request.POST.get("FirstName"))
        print("Last Name:", request.POST.get("LastName"))
        print("Date & Time:", str(request.POST.get("DateTime")).split("T"))
        print("Player Count:", request.POST.get("PlayerCount"))        

    return render(request, "createbooking.html", {})


def register_view(request):
    return render(request, "register.html", {})


def login_view(request):
    return render(request, "login.html", {})