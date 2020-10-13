# from django.shortcuts import render, HttpResponseRedirect
# from django.contrib.auth.forms import AuthenticationForm
# def login(request):
#     if request.method == "POST:
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/app/')
#     else:
#         form = 
from django.shortcuts import render, HttpResponseRedirect
from rameniaapp.forms import RegistrationForm
from rameniaapp.models import Profile
from django.contrib.auth import authenticate, login

def register(request):
    BLANK_METADATA = {"Rated": 0, "Tried": 0, "Reviewed": 0, "Reputation": 0, \
    "Description": "", "Entries Made": 0}
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            if request.FILES:
                file = list(request.FILES.keys())[0]
                profile = Profile(name=form.cleaned_data["profile_name"], \
                                profile_pic=request.FILES[file], \
                                user=user, metadata=BLANK_METADATA)
                profile.save()
            else:
                profile = Profile(name=form.cleaned_data["profile_name"], \
                                user=user, metadata=BLANK_METADATA)
                profile.save()
            #Backend param is not specified if this isn't done first
            user = authenticate(username=form.cleaned_data["username"],\
                                password=form.cleaned_data["password1"])
            login(request, user)
            return HttpResponseRedirect('/app/')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {"form": form})
