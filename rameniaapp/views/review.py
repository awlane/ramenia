from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from rameniaapp.forms import ReviewForm
from rameniaapp.models import Review, ReviewImage, Noodle
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rameniaapp.actionhookutils import dispatch_hook

def ramen_review_view(request,noodle_id):
    form = ReviewForm()
    noodle = Noodle.objects.get(pk=noodle_id)
    # If this is a POST request then process the Form data
    if request.user.is_authenticated:
        if request.method == "POST":
           # Create a form instance and populate it with data from the request of the user
            form = ReviewForm(request.POST or None)
            #Check if the form is valid:
            if form.is_valid():
                previous_review = Review.objects.filter(noodle = noodle, reviewer = request.user)
                if previous_review:
                    previous_review[0].delete()
                data = form.save(commit=False)
               # data.title = request.POST["body"]
               # data.body = request.POST["body"]
               # data.rating = request.POST["rating"]
                data.reviewer = request.user
                data.noodle = noodle
                data.save()
                if request.FILES:
                    file = list(request.FILES.keys())[0]
                    image = request.FILES[file]
                    review_image = ReviewImage(image = image, review = data, uploader = request.user)
                    review_image.save()
                if not previous_review:
                    request.user.profile.increment_meta_val("Reviewed", 1)
                    dispatch_hook(request.user, "review-created", count=request.user.profile.get_meta_val("Reviewed"))

    return HttpResponseRedirect(reverse('noodle', kwargs={"noodle_id" : noodle.id}))
