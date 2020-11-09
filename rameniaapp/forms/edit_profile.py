from django import forms
from rameniaapp.models import Profile
from django.forms.widgets import TextInput, Textarea

class EditProfileForm(forms.Form):
     profile_name = forms.CharField(label="Profile Name", max_length=80, widget=TextInput(attrs={'class':'form-control'}))
     profile_pic = forms.ImageField(label="Profile Picture", required=False, widget=TextInput(attrs={'class':'form-control'}))
     description = forms.CharField(label= "Description", max_length=300, required=False, widget=TextInput(attrs={'class':'form-control'}))

     # class meta:
     #      model = Profile
     #      fields = (
     #                'profile_name'
     #                'profile_pic'
     #                'description'
     #           )
     