from django import forms
from .models import BookingModel



class BookingForm(forms.ModelForm):
    """Form for the user to create a booking"""

    class Meta:
        """Self explanitory metadata"""
        model = BookingModel
        fields = [ 'DateTime', 'NumberOfPlayers' ]
        widgets = {
            'DateTime': forms.DateTimeInput(attrs={'type': 'datetime-local', 'format':'%d/%m/%Y, %H:%M'}),
            'NumberOfPlayers': forms.NumberInput(attrs={'min':1, 'max':16, 'value':1})
        }