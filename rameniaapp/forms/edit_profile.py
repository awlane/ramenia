from django import forms
from rameniaapp.models import Profile
from django.contrib.auth.forms import UserChangeForm

class EditProfileForm(UserChangeForm):

     profile_name = forms.CharField(label="Profile Name", max_length=80)
     profile_pic = forms.ImageField(label="Profile Picture")
     description = forms.CharField(label= "Description", max_length=300)

     # class meta:
     #      model = Profile
     #      fields = (
     #                'profile_name'
     #                'profile_pic'
     #                'description'
     #           )
     