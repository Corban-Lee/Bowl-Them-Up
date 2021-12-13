from django import forms  

class BookingFormCreate(forms.Form):
    FirstName = forms.CharField(label="Enter first name: ",max_length=64)  
    LastName  = forms.CharField(label="Enter last name: ", max_length = 64)  
    DateTime  = forms.DateTime(label="Enter date: ")
    NumberOfPlayers  = forms.IntegerField(label="Enter last name", max_length = 10)
    Email  = forms.EmailField(label="Enter email: ", max_length = 64)
    PhoneNumber  = forms.CharField(label="Enter phone number", max_length = 11)

class BookingFormEdit(forms.Form):
    FirstName = forms.CharField(label="Enter first name: ",max_length=64)  
    LastName  = forms.CharField(label="Enter last name: ", max_length = 64)  
    DateTime  = forms.DateTime(label="Enter date: ")
    NumberOfPlayers  = forms.IntegerField(label="Enter last name", max_length = 10)
    Email  = forms.EmailField(label="Enter email: ", max_length = 64)
    PhoneNumber  = forms.CharField(label="Enter phone number", max_length = 11)

class BookingFormDelete(forms.Form):
    FirstName == 0  
    LastName  == 0
    DateTime  == 0
    NumberOfPlayers  == 0
    Email  == 0
    PhoneNumber  == 0