from django import forms

from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'brand', 'transmission', 'number_plate',
            'price', 'longitude', 'latitude',
            'available'
        ]
