from django.db import models
from django.conf import settings
from .noodle import Noodle

class List(models.Model):
    name = models.CharField(max_length=60)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    noodles = models.ManyToManyField(Noodle, blank=True)
