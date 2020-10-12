from django.shortcuts import render, HttpResponse
from django.template import loader
from django.conf import settings
from django.db.models import Avg
from rameniaapp.models import Noodle, NoodleImage, List, Profile

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
