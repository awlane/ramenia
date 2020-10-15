from django.shortcuts import render, HttpResponse
from django.template import loader
from django.conf import settings
from django.db.models import Avg
from rameniaapp.models import Noodle
from rameniaapp.forms import SearchForm

def view_search(request):
    template = loader.get_template('search.html')
    context = {}
    return HttpResponse(template.render(context, request))
