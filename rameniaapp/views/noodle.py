from django.shortcuts import render, HttpResponse
from django.template import loader
from django.conf import settings
from django.db.models import Avg
from rameniaapp.models import Noodle
from .edit_util import apply_change

def view_noodle(request, noodle_id):
    noodle = Noodle.objects.get(pk=noodle_id)
    avg_rating = noodle.review_set.all().aggregate(Avg('rating'))["rating__avg"]
    template = loader.get_template('ramen.html')
    context = { "noodle" : noodle, "MEDIA_URL" : settings.MEDIA_URL,
                "avg_rating" : avg_rating }
    if len(noodle.edit_set.all()) > 0:
        for edit in noodle.edit_set.all():
            apply_change(edit)
    from rameniaapp.models import Edit
    if len(Edit.objects.filter(noodle=None)) > 0:
        for edit in Edit.objects.filter(noodle=None):
            apply_change(edit)
    return HttpResponse(template.render(context, request))