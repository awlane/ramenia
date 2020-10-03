from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    profile_name = forms.CharField(label="Profile Name (this is not used to login)", max_length=80)
    profile_pic = forms.ImageField(label="Profile Picture")