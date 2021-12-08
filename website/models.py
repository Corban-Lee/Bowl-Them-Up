from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ForeignKey

class Customer(models.Model):
    """Customers. These are the people that use the website and book games with the bowling alley"""
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=64, unique=True)
    FirstName = models.CharField(max_length=64)
    LastName = models.CharField(max_length=64)
    PhoneNumber = models.CharField(max_length=10)
    Email = models.EmailField(max_length=128)
    Password = models.CharField(max_length=64)

class Player(models.Model):
    """These are the people that show up to play a game at the bowling alley"""
    PlayerID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=64)
    LastName = models.CharField(max_length=64)
    ShoeSize = models.IntegerField()
    BallSize = models.IntegerField()

class AlleyLane(models.Model):
    """This entity represents a lane in the bowling alley"""
    AlleyLaneID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=32)
    Status = models.CharField(max_length=32, default="closed")

class Bookings(models.Model):
    """Similar to an online order. This entity contains information regarding a customers arangement to use a bowling alley lane."""
    BookingsID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    PlayerID = models.ForeignKey(to=Player, on_delete=models.CASCADE)
    AlleyLaneID = models.ForeignKey(to=AlleyLane, on_delete=models.CASCADE)
    NumberOfPlayers = models.IntegerField()
    Date = models.DateField(null=False)
    Time = models.TimeField(null=False)
    Status = models.CharField(max_length=32)