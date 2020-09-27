from django.shortcuts import render, HttpResponse
from django.template import loader
from django.conf import settings
from rameniaapp.models import Noodle

def view_noodle(request, noodle_id):
    noodle = Noodle.objects.get(pk=noodle_id)

    template = loader.get_template('ramen.html')
    context = { "noodle" : noodle, "MEDIA_URL" : settings.MEDIA_URL}
    return HttpResponse(template.render(context, request))