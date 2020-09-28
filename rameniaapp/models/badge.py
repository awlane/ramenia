from django.db import models
from django.conf import settings

class Badge(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=140)
    #TODO: Only allowing blank for testing purposes, we will want to change this when we clean up UI
    image = models.ImageField(blank=True)
