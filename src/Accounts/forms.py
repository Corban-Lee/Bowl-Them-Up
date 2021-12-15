from typing import Pattern
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Account

class CreateUserForm(UserCreationForm):
	class Meta:
		model = Account
		fields = ['FirstName', 'LastName', 'PhoneNumber', 'EmailAddress', 'password1', 'password2']

	FirstName = forms.CharField(label='First Name', max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'John'}))
	LastName = forms.CharField(label='Last Name', max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Doe'}))
	PhoneNumber = forms.IntegerField(label='Phone Number', widget=forms.NumberInput(attrs={'placeholder': '09758958432', 'size': 11, 'onKeyDown' : "if(this.value.length==11 && event.keyCode!=8) return false;"}))
	EmailAddress = forms.EmailField(label='Email Address', required=True, widget=forms.EmailInput(attrs={'placeholder': 'johndoe@example.com'}))
	password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(label='Confirm Password', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	# password1 and password2 --> Password and Confirmation Password
	# Django vocab ^

