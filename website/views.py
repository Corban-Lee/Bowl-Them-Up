from django.shortcuts import render

##############################################################

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

def login(request):
    return render(request, "views/login.html")

##############################################################

# Create processes here.

from .forms import RegisterAccountForm

def register_account_form(request):
    if request.method != "POST": return

    form = RegisterAccountForm(request.POST)
    if form.is_valid():
        pass

    


    return render(request, "views/login.html")