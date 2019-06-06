from django import forms
from .models import *

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Hoods
        exclude = ['population', 'admin','timestamp']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'hood_id']
