from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Account

class CreateUserForm(UserCreationForm):
	class Meta:
		model = Account
		fields = ['FirstName', 'LastName', 'PhoneNumber', 'EmailAddress', 'password1', 'password2']

	FirstName = forms.CharField(label='First Name', max_length=30, required = True, widget=forms.TextInput(attrs={'class': 'form-register'}))
	LastName = forms.CharField(label='Last Name', max_length=30, required = True, widget=forms.TextInput(attrs={'class': 'form-register'}))
	PhoneNumber = forms.CharField(label='Last Name', max_length=11, widget=forms.TextInput(attrs={'class': 'form-register'}))
	EmailAddress = forms.EmailField(label='Email Address', required = True, widget=forms.TextInput(attrs={'class': 'form-register'}))
	password1 = forms.CharField(label='Password', required = True, widget=forms.PasswordInput(attrs={'class': 'form-register'}))
	password2 = forms.CharField(label='Confirm Password',  required = True, widget=forms.PasswordInput(attrs={'class': 'form-register'}))
