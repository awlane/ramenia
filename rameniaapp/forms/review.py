from django import forms
from rameniaapp.models import Review

class ReviewForm(forms.Form):
    class Meta:
          model = Review
          fields = (
                     'image',
                     'noodle',
                     'reviewer'
          )