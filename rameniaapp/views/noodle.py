from django.shortcuts import render, HttpResponse
from django.template import loader
from django.conf import settings
from django.db.models import Avg
from rameniaapp.models import Noodle
from .edit_util import apply_change
from rameniaapp.forms import ReviewForm

def view_noodle(request, noodle_id):
    '''View to render noodle page'''
    noodle = Noodle.objects.get(pk=noodle_id)
    # Update noodle review score on load- could be area to optimize
    avg_rating = noodle.review_set.all().aggregate(Avg('rating'))["rating__avg"]
    # If no reviews are submitted, rating is returned as None (ie null)
    # rather than 0. This prevents that and cleans up trailing decimals.
    if not avg_rating:
        avg_rating = 0.0 
    if avg_rating > 0:
        avg_rating = round(avg_rating, 1)
    template = loader.get_template('ramen.html')
    context = { "noodle" : noodle, "MEDIA_URL" : settings.MEDIA_URL,
                "avg_rating" : avg_rating, 'form': ReviewForm() }
    return HttpResponse(template.render(context, request))