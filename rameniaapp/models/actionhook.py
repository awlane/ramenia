from django.db import models

class ActionHook(models.Model):
    hook_name = models.CharField(max_length=80)
    params = models.JSONField()
