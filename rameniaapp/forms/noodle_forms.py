from django import forms
from django.forms.widgets import TextInput
from rameniaapp.models import Edit
from rameniaapp.models import Tag

class TagsField(forms.Field):
    # This code based on example code in Django docs
    # https://docs.djangoproject.com/en/3.1/ref/forms/validation/
    def to_python(self, value):
        if not value:
            return []
        return value.split(',')

    def validate(self, value):
        super().validate(value)

class NoodleForm(forms.Form):
    name = forms.CharField(max_length=50)
    manufacturer = forms.CharField(max_length=50)
    description = forms.CharField(max_length=200)
    flavor = forms.CharField(max_length=50)
    released = forms.CharField(max_length=50)
    line = forms.CharField(max_length=50)
    tags = TagsField(widget=TextInput, required=False)

class AddNoodleForm(NoodleForm):
    image = forms.ImageField(required = True)

class EditNoodleForm(NoodleForm):
    image = forms.ImageField(required = False)