from django import forms
from rameniaapp.models import Review, ReviewImage
from rameniaapp.models import Tag

class ReviewRamenForm(forms.Form):
    ONE_STAR = 1
    TWO_STAR = 2
    THREE_STAR = 3
    FOUR_STAR = 4
    FIVE_STAR = 5

    title = forms.CharField(max_length=60)
    body = forms.CharField(max_length=1000)
  #  rating = forms.IntegerField(choices=Ratings.choices)