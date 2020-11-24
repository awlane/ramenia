from django.db import models
from django.conf import settings

class Edit(models.Model):
    # If multi-image adding is added, better to credit multiple Edit objs
    # and approve piecemeal
    image = models.ImageField(blank=True)
    # Store change as a JSON to simplify any changes to Noodle
    # Expected Fields:
    # Name, Line, Flavor, Description, Manufacturer, Released
    change = models.JSONField(null=True, blank=True)
    noodle = models.ForeignKey("rameniaapp.Noodle", null=True, blank=True, on_delete=models.CASCADE)
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now=True)