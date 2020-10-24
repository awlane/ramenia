from django import forms
from rameniaapp.models import Edit
from .edit import EditForm
from rameniaapp.models import Tag

class EditRamenForm(forms.Form):
    name = forms.CharField(max_length=50)
    manufacturer = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    flavor = forms.CharField(max_length=50)
    released = forms.CharField(max_length=50)
    line = forms.CharField(max_length=50)
    image = forms.ImageField(required = False)