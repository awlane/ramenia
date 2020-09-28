from django.db import models
from django.conf import settings
from .badge import Badge

class Profile(models.Model):
    name = models.CharField(max_length=30)
    #TODO: Use this as a container for bio and stats
    metadata = models.JSONField(null=True, blank=True)
    #TODO: Rather than modify user model from base, this can be used to store site configuration
    preferences = models.JSONField(null=True, blank=True)
    profile_pic = models.ImageField(blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #User can have no badges!
    badges = models.ManyToManyField("rameniaapp.Badge", blank=True)    