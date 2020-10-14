from django import forms

class ListCreateForm(forms.Form):
    list_name = forms.CharField(label="Name", max_length=60)
