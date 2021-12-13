from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Templates/thanks.html", {'form': form})
        else:
            return render(request, "Templates/register.html", {'form': form})
    else:
        if request.user.is_authenticated:
            return render(request, "Templates/index.html")
        form = CreateUserForm()
        return render(request, "Templates/signup.html", {'form': form})

def loginPage(request):
    # Note: Dont name the function login() as this is a built-in function.
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, "Templates/index.html")

def create(request):
    return render(request, 'register.html', {})


def login(request):
    return render(request, 'login.html', {})


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
