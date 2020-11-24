from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import FileInput

class RegistrationForm(UserCreationForm):
    '''Form for user registration that allows profile setup'''
    profile_name = forms.CharField(label="Profile Name (this is not used to login)", max_length=80)
    profile_pic = forms.ImageField(label="Profile Picture", required=False, widget=FileInput(attrs={'class':'form-control-file'}))
    
    def __init__(self, *args, **kwargs):
        # This is the correct place to override the bootstrap styling
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.widget = forms.TextInput(attrs={'class':'tag_field'})
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['password1'].widget.attrs.update({'class':'form-control'})
        self.fields['password2'].widget.attrs.update({'class':'form-control'})
        self.fields['profile_name'].widget.attrs.update({'class':'form-control'})