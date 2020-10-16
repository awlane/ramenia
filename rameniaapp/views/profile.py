from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.contrib.auth.models import User
from rameniaapp.forms import EditProfileForm


def view_profile(request, user_id):
    profile = User.objects.get(pk=user_id).profile
    template = loader.get_template('profile.html')
    context = { "profile" : profile, "MEDIA_URL" : settings.MEDIA_URL }
    return HttpResponse(template.render(context, request))

def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = request.user.profile
            if form.cleaned_data["profile_name"]:
                profile.name = form.cleaned_data["profile_name"]
            if form.cleaned_data["description"]:
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