from django import forms
from django.forms import Textarea
from rameniaapp.models import Review, ReviewImage
from rameniaapp.models import Tag

class ReviewForm(forms.ModelForm):
    image = forms.ImageField(required = False)
    class Meta:
        model = Review
        fields = ["title", "body", "rating"]
        widgets = {
            'body': Textarea(attrs={'cols': 40, 'rows': 10}),
        }
