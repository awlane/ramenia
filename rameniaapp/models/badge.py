from django.db import models
from django.conf import settings

class Badge(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=140)
    # If badges are ever generated without manually adding them,
    # change to ensure correct validation
    image = models.ImageField(blank=True)
