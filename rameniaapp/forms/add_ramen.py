from django import forms
from django.forms import Textarea
from rameniaapp.models import Ramen

class AddRamenForm(forms.ModelForm):
    class Meta:
        model = Ramen
        fields = ["name", "manufacturer", "description"]