from django.db import models
from .noodle import Noodle

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=140)