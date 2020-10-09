from django.db import models
from django.conf import settings

class Edit(models.Model):
    image = models.ImageField(blank=True)
    change = models.JSONField(null=True, blank=True)
    noodle = models.ForeignKey("rameniaapp.Noodle", null=True, blank=True, on_delete=models.CASCADE)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)