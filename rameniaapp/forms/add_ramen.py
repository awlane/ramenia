from django import forms
from django.forms import Textarea
from rameniaapp.models import AddRamen

class AddRamenForm(forms.ModelForm):
    class Meta:
        model = AddRamen
        fields = ["name", "manufacturer", "description"]