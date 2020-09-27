from django.db import models

class Noodle(models.Model):
    name = models.CharField(max_length=60)
    #TODO: Validations and character limit enforcement will be dealt with later
    metadata = models.JSONField(null=True, blank=True)
    tags = models.ManyToManyField("rameniaapp.Tag", blank=True)
    #Currently assume that noodles are editable.
    timestamp = models.DateField(auto_now=True)

class NoodleImage(models.Model):
    #TODO: Change this value to a more formal directory 
    image = models.ImageField()
    noodle = models.ForeignKey(Noodle, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)