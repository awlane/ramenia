from django import forms
from django.forms.widgets import TextInput

class ListCreateForm(forms.Form):
    list_name = forms.CharField(label="Name", max_length=60, widget=TextInput(attrs={'class':'form-control'}))
