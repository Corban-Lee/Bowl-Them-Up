from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

class Customer(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=64, unique=True)
    FirstName = models.CharField(max_length=64)
    LastName = models.CharField(max_length=64)
    PhoneNumber = models.CharField(max_length=10)
    Email = models.EmailField(max_length=128)
    Password = models.CharField(max_length=64)

class Player(models.Model):
    PlayerID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=64)
    LastName = models.CharField(max_length=64)
    ShoeSize = models.IntegerField()
    BallSize = models.IntegerField()

class AlleyLane(models.Model):
    AlleyLaneID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=32)
    models.CharField(max_length=32)

class Bookings(models.Model):
    BookingsID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    PlayerID = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    AlleyLaneID = models.ForeignKey(to=AlleyLane, on_delete=models.CASCADE)
    NumberOfPlayers = models.IntegerField()
    Date = models.DateField(null=False)
    Time = models.TimeField(null=False)
    Status = models.CharField(max_length=32)