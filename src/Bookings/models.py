from django.db import models

# Create your models here.

from Accounts.models import Account


class AlleyLane(models.Model):
    AlleyLaneID = models.AutoField(primary_key=True)
    Available   = models.BooleanField(null=False, default=False)


class Player(models.Model):
    PlayerID   = models.AutoField(primary_key=True)
    ShoeSize   = models.IntegerField(default=False)
    BallSize   = models.IntegerField(default=False)


class Booking(models.Model):
    BookingID   = models.AutoField(primary_key=True)
    CustomerID  = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    AlleyLaneID = models.ForeignKey(to=AlleyLane, on_delete=models.CASCADE)
    Players     = models.ManyToManyField(Player)
    NumberOfPlayers = models.IntegerField()
    DateTime    = models.DateTimeField(null=False)



