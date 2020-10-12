from django.shortcuts import render, HttpResponse
from django.template import loader
from django.conf import settings
from rameniaapp.models import Noodle, NoodleImage

def view_list(request, list_id):
    noodles = Noodle.objects.all()
    images = []
    for noodle in noodles:
        image = NoodleImage.objects.filter(noodle__pk=noodle.id)[0]
        images.append(image)
    print(images)
    template = loader.get_template('list.html')
    context = { "noodles" : zip(noodles, images), "MEDIA_URL" : settings.MEDIA_URL }
    return HttpResponse(template.render(context, request))
