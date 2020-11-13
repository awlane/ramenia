from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.forms.widgets import TextInput

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class':'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class':'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class':'form-control'})