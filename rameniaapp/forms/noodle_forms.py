from django import forms
from django.forms.widgets import TextInput, Textarea, FileInput
from rameniaapp.models import Edit
from rameniaapp.models import Tag

class TagsField(forms.Field):
    '''Field for specifying expected tags and turning input strings into usable data'''
    # This code based on example code in Django docs
    # https://docs.djangoproject.com/en/3.1/ref/forms/validation/
    def to_python(self, value):
        if not value:
            return []
        return value.split(',')

    def validate(self, value):
        super().validate(value)

class NoodleForm(forms.Form):
    '''Generic class for noodle fields, couldn't use modelform due to JSON, do not use in views'''
    name = forms.CharField(max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    manufacturer = forms.CharField(max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=200, widget=Textarea(attrs={'class':'form-control'}))
    flavor = forms.CharField(max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    released = forms.CharField(max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    line = forms.CharField(max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    tags = TagsField(required=False, widget=TextInput(attrs={'class':'form-control'}))

class AddNoodleForm(NoodleForm):
    '''Form for add noodle view'''
    image = forms.ImageField(required = False, widget=FileInput(attrs={'class':'form-control-file'}))

class EditNoodleForm(NoodleForm):
    '''Form for edit noodle view'''
    image = forms.ImageField(required = False, widget=FileInput(attrs={'class':'form-control-file'}))
