from django.db import models
from django.conf import settings

class Noodle(models.Model):
    name = models.CharField(max_length=60)
    #TODO: Validations and character limit enforcement are in forms
    metadata = models.JSONField(null=True, blank=True)
    tags = models.ManyToManyField("rameniaapp.Tag", blank=True)
    #Currently assume that noodles are editable and we want a history
    timestamp = models.DateField(auto_now=True)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

class NoodleImage(models.Model):
    image = models.ImageField()
    noodle = models.ForeignKey(Noodle, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)