from django import forms
from rameniaapp.models import Edit

class EditForm(forms.Form):
    class Meta:
          model = Edit
          fields = (
                     'image',
                     'noodle',
                     'editor'
          )