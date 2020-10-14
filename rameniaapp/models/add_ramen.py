from django.db import models
from django.conf import settings


class Ramen(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    description = models.TextField(max_length=400)