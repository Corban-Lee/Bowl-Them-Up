from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, "register.html", {'form': form})
        return redirect("/")
    else:
        if request.user.is_authenticated:
            return render(request, "index.html")
        form = CreateUserForm()
        return render(request, "register.html", {'form': form})

def loginPage(request):
    # Note: Dont name the function login() as this is a built-in function.
    if request.method == "POST":
        EmailAddress = request.POST.get('EmailAddress')
        password = request.POST.get('password')
        user = authenticate(request, EmailAddress=EmailAddress, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    else:
        return render(request, 'login.html', {})

def signoutPage(request):
    logout(request=request)
    return redirect("/")

def account(request, username):
    """
    view the user's account
    """
    pass


def edit(request, username):
    """
    edit the user's account
    """
    pass


def delete(request, username):
    """
    delete the user's account
    """
    pass
