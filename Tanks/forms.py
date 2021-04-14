from django.forms import ModelForm
from django import forms
from .models import Tank

class TankForm(ModelForm):
    class Meta:
        model = Tank
        fields = '__all__'

NAME_CHOICES = [
    ('Type_10', 'Type 10'),
    ('K2_Black_Panther', 'K2 Black Panther PIP'),
    ('T-14_Armata', 'T-14 Armata'),
    ('Merkava', 'Merkava Mk 4M Windbreaker'),
    ('Type_99_tank', 'Type 99A'),
    ('Leopard_2', 'Leopard 2A7+'),
    ('M1_Abrams', 'M1A2C SEPv3 Abrams'),
    ('Challenger_2', 'Challenger 2 LEP'),
    ('Leclerc_tank', 'Leclerc XLR'),
]

ID_CHOICES = [
    ('414', 'Type 10'),
    ('289', 'K2 Black Panther PIP'),
    ('905', 'T-14 Armata'),
    ('39', 'Merkava Mk 4M Windbreaker'),
    ('263', 'Type 99A'),
    ('37', 'Leopard 2A7+'),
    ('1', 'M1A2C SEPv3 Abrams'),
    ('11', 'Challenger 2 LEP'),
    ('100', 'Leclerc XLR'),
]

class NamesForm(forms.Form): # for DBpedia's API name
    name = forms.CharField(label='Select a tank from the list to get an abstract on', widget = forms.Select(choices = NAME_CHOICES))

class IDForm(forms.Form): # for www.militaryfactory.com's ID
    id = forms.CharField(label="Select a tank from the list to get www.militaryfactory.com's article on", widget = forms.Select(choices = ID_CHOICES))