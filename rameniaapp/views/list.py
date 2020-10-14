from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.db.models import Avg
from rameniaapp.models import Noodle, NoodleImage, List, Profile
from rameniaapp.forms import ListCreateForm
from django.contrib.auth.models import User
from django.urls import reverse

def view_list(request, list_id):
    list = List.objects.get(pk=list_id)
    profile = Profile.objects.get(user__pk=list.user.id)
    noodles = list.noodles.all()
    images = []
    review_avgs = []
    
    for noodle in noodles:
        image = NoodleImage.objects.filter(noodle__pk=noodle.id)[0]
        avg_rating = noodle.review_set.all().aggregate(Avg('rating'))["rating__avg"]
        images.append(image)
        review_avgs.append(avg_rating)
        
    template = loader.get_template('list.html')
    context = { "listinfo" : list,
                "profile" : profile,
                "noodles" : zip(noodles, images, review_avgs),
                "MEDIA_URL" : settings.MEDIA_URL }
    return HttpResponse(template.render(context, request))

def view_user_lists(request, user_id):
    user = User.objects.get(pk=user_id)
    lists = List.objects.filter(user__pk=user_id).all()
    is_my_lists = (request.user.is_authenticated and request.user.id == user.id)

    if request.method == "POST":
        form = ListCreateForm(request.POST)
        if form.is_valid and is_my_lists:
            new_list = List.objects.create(name=form.data['list_name'], user=user)
            new_list.save()
            return HttpResponseRedirect(reverse("user_lists", args=[user_id]))

    template = loader.get_template('user_lists.html')
    context = { "lists" : lists, "lists_user" : user, "is_my_lists" : is_my_lists }
    return HttpResponse(template.render(context, request))
