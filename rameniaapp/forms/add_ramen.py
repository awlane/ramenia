from django import forms
from rameniaapp.models import Edit
from .edit import EditForm

class RamenForm(EditForm):
    name = forms.CharField(max_length=50)
    manufacturer = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    flavor = forms.CharField(max_length=50)
    released = forms.CharField(max_length=50)
    line = forms.CharField(max_length=50)
    # image = forms.ImageField(blank=True)
    
    class Meta(EditForm.Meta):
        fields = EditForm.Meta.fields + ("name",)

