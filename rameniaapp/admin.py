from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Noodle)
admin.site.register(Tag)
admin.site.register(NoodleImage)