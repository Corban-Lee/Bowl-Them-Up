from django import forms

class RegisterAccountForm(forms.Form):
    FirstName = forms.CharField(label="First Name", max_length=64)
    LastName  = forms.CharField(label="Last Name", max_length=64)
    Username  = forms.CharField(label="Username", max_length=64)
    Password  = forms.CharField(label="Password", max_length=64)
    ConfirmedPassword = forms.CharField(label="Confirmed Password", max_length=64)
    EmailAddress = forms.CharField(label="Email Address", max_length=128)
    PhoneNumber  = forms.CharField(label="Phone Number", max_length=10)
    print("created form")