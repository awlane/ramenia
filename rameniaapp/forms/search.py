from django import forms
from django.forms.widgets import TextInput

class SearchForm(forms.Form):
    text_search = forms.CharField(label="Search", max_length=100, widget=TextInput(attrs={'class':'form-control'}))
