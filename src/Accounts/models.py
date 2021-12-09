from django.db import models

# Create your models here.

class Account(models.Model):
    UserID       = models.AutoField(primary_key=True)
    FirstName    = models.CharField(max_length=64)
    LastName     = models.CharField(max_length=64)
    PhoneNumber  = models.CharField(max_length=10)
    EmailAddress = models.EmailField(max_length=128)
    Password     = models.CharField(max_length=64)
