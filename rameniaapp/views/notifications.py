from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.contrib.auth.models import User
from rameniaapp.forms import EditProfileForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="/app/login")
def view_notifications(request):
    template = loader.get_template('notifications.html')
    context = { }
    return HttpResponse(template.render(context, request))
