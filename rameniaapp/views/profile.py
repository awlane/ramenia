from django.shortcuts import render, HttpResponse
from django.template import loader
from django.conf import settings
from rameniaapp.models import Profile

def view_profile(request, profile_id):
    noodle = Profile.objects.get(pk=profile_id)
    template = loader.get_template('profile.html')
    context = { "profile" : noodle, "MEDIA_URL" : settings.MEDIA_URL }
    return HttpResponse(template.render(context, request))