from django.db import models
from django.conf import settings
from datetime import date

class Noodle(models.Model):
    name = models.CharField(max_length=60)
    #TODO: Validations and character limit enforcement are in forms
    # JSON generally assumes following fields: 
    # Line, Flavor, Description, Manufacturer, Released
    metadata = models.JSONField(null=True, blank=True)
    tags = models.ManyToManyField("rameniaapp.Tag", blank=True)
    # Currently assume that noodles are editable and we want a history
    created_timestamp = models.DateField(auto_now=False, default=date.today)
    edited_timestamp = models.DateField(auto_now=False, default=date.today)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

# Because of the one to many relationship of reviews/photos, create a separate model
class NoodleImage(models.Model):
    image = models.ImageField(default="noodles.png")
    main = models.BooleanField(default=False)
    noodle = models.ForeignKey(Noodle, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=False, default=date.today)
    is_default = models.BooleanField(default=False)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
