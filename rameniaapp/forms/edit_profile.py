from django import forms
from rameniaapp.models import Profile

class EditProfileForm(forms.Form):
     profile_name = forms.CharField(label="Profile Name", max_length=80)
     profile_pic = forms.ImageField(label="Profile Picture", required=False)
     description = forms.CharField(label= "Description", max_length=300, required=False)

     # class meta:
     #      model = Profile
     #      fields = (
     #                'profile_name'
     #                'profile_pic'
     #                'description'
     #           )
     