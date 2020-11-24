from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput

class PrettyAuthenticationForm(AuthenticationForm):
    '''django.auth AuthenticationForm with Bootstrap styling override'''
    def __init__(self, *args, **kwargs):
        super(PrettyAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['password'].widget.attrs.update({'class':'form-control'})