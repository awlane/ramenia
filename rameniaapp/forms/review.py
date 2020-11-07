from django import forms
from django.forms import Textarea, Select, TextInput
from rameniaapp.models import Review, ReviewImage
from rameniaapp.models import Tag

class ReviewForm(forms.ModelForm):
    image = forms.ImageField(required = False)
    class Meta:
        model = Review
        fields = ["title", "body", "rating"]
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'rating': Select(attrs={'class':'form-control'}),
            'body': Textarea(attrs={'class':'form-control', 'cols': 40, 'rows': 10}),
        }
