from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm

# Creating an Account for BowlThemUp
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
 
# Logging in an Account for BowlThemUp
def loginPage(request):
    if request.method == "POST":
        EmailAddress = request.POST.get('EmailAddress')
        password = request.POST.get('password')
        user = authenticate(request, EmailAddress=EmailAddress, password=password)
        if user is not None:
            login(request, user)
        else:
            return render(request, 'login.html', {"error_message":"Account has not been found. Please Try again"})
        return redirect("/")
    else:
        return render(request, 'login.html', {})

def signoutPage(request):
    logout(request=request)
    return redirect("/")
