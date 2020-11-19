from django import forms
from rameniaapp.models import Profile
from django.forms.widgets import TextInput, Textarea, FileInput

class EditProfileForm(forms.Form):
     '''Form for edit profile view'''
     profile_name = forms.CharField(label="Profile Name", max_length=80, widget=TextInput(attrs={'class':'form-control'}))
     profile_pic = forms.ImageField(label="Profile Picture", required=False, widget=FileInput(attrs={'class':'form-control-file'}))
     description = forms.CharField(label= "Description", max_length=300, required=False, widget=TextInput(attrs={'class':'form-control'}))