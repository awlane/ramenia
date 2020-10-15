from django import forms

class SearchForm(forms.Form):
    text_search = forms.CharField(label="Search", max_length=100)
