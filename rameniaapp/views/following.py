from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.contrib.auth.models import User
from rameniaapp.forms import EditProfileForm
from django.views.decorators.csrf import csrf_exempt

def view_following (request, user_id):
    user = User.objects.get(pk=user_id)
    following = user.profile.following.all()
    followers = user.profile.followers.all()
    template = loader.get_template('following.html')
    context = { "following" : following , "followers" : followers, "profile" : user.profile, "MEDIA_URL" : settings.MEDIA_URL }
    return HttpResponse(template.render(context, request))
