from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.contrib.auth.models import User
from rameniaapp.forms import EditProfileForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rameniaapp.actionhookutils import dispatch_hook

def view_profile(request, user_id):
    profile = User.objects.get(pk=user_id).profile
    template = loader.get_template('profile.html')
    following = False
    if request.user.is_authenticated:
        following = request.user.profile in profile.followers.all()
    context = { "profile" : profile, "MEDIA_URL" : settings.MEDIA_URL, "following": following}
    return HttpResponse(template.render(context, request))

@login_required(login_url="/app/login")
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = request.user.profile
            profile.name = form.cleaned_data["profile_name"]
            profile.metadata["Description"] = form.cleaned_data["description"]
            if request.FILES:
                file = list(request.FILES.keys())[0]
                profile.profile_pic = request.FILES[file]
            profile.save()
        return HttpResponseRedirect('/app/')
    else:
        initial = {'profile_name' : request.user.profile.name,\
                    'description' : request.user.profile.metadata["Description"]}
        form = EditProfileForm(initial=initial)
    return render(request, 'registration/edit_profile.html', {"form": form})

@csrf_exempt
@login_required(login_url="/app/login")
def follow_profile(request, user_id):
    if request.method == "POST":
        profile = User.objects.get(pk=user_id).profile
        profile.followers.add(request.user.profile)
        dispatch_hook(request.user, "user-followed")
        return HttpResponse(status=200)
    elif request.method == "DELETE":
        profile = User.objects.get(pk=user_id).profile
        profile.followers.remove(request.user.profile)
        dispatch_hook(request.user, "user-unfollowed")
        return HttpResponse(status=200)
