from django.shortcuts import render, HttpResponse
from django.template import loader
from django.conf import settings
from django.contrib.auth.models import User

def view_profile(request, user_id):
    profile = User.objects.get(pk=user_id).profile
    template = loader.get_template('profile.html')
    context = { "profile" : profile, "MEDIA_URL" : settings.MEDIA_URL }
    return HttpResponse(template.render(context, request))
