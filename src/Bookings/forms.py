from django import forms


class NewBookingForm(forms.Form):
    Date            = forms.DateField(    required=True, label='Booking Date',      widget=forms.DateTimeInput( attrs={'type': 'date'               } ) )
    Time            = forms.TimeField(    required=True, label='Booking Time',      widget=forms.TimeInput(     attrs={'type': 'time', 'step': 1800 } ) )
    NumberOfPlayers = forms.IntegerField( required=True, label='Number of Players', widget=forms.NumberInput(   attrs={'min': 1, 'max': 16          } ) )