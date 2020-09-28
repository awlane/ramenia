from django.contrib import admin
from django.apps import apps

# Register your models here.
from .models import *

app = apps.get_app_config('rameniaapp')

for name, model in app.models.items():
    admin.site.register(model)