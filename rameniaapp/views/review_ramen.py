from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from rameniaapp.forms import ReviewRamenForm
from rameniaapp.models import Review, ReviewImage

def review_view(request, noodle_id):
    review = Review.objects.filter(pk=noodle_id)
    #avg_rating = noodle.review_set.all().aggregate(Avg('rating'))["rating__avg"]
    template = loader.get_template('review_ramen.html')
    context = { "noodle" : noodle, "MEDIA_URL" : settings.MEDIA_URL,
                }
    return HttpResponse(template.render(context, request))

  