from django.db import models
from django.forms.models import modelformset_factory

# Create your models here.

from Accounts.models import Account


class LaneModel(models.Model):
    """Model for the alley lanes in the bowling alley"""

    Id = models.AutoField(primary_key=True)
    Available   = models.BooleanField(null=False, default=False)


class BookingModel(models.Model):
    """Model for the customer created bookings"""

    Id              = models.AutoField(primary_key=True)
    Customer        = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    Lane            = models.ForeignKey(to=LaneModel, on_delete=models.CASCADE)
    DateTime        = models.DateTimeField(null=False)
    NumberOfPlayers = models.IntegerField(null=False)



