from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from rameniaapp.forms import ReviewForm
from rameniaapp.models import Review, ReviewImage, Noodle
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rameniaapp.actionhookutils import dispatch_hook
from django.contrib import messages

def ramen_review_view(request,noodle_id):
    '''View to handle noodle review form'''
    form = ReviewForm()
    noodle = Noodle.objects.get(pk=noodle_id)
    # If this is a POST request then process the Form data
    if request.user.is_authenticated:
        if request.method == "POST":
           # Create a form instance and populate it with data from the request of the user
            form = ReviewForm(request.POST or None)
            # Check if the form is valid:
            if form.is_valid():
                previous_review = Review.objects.filter(noodle = noodle, reviewer = request.user)
                # We only want the latest review; this also helps prevent manipulation of ratings
                if previous_review:
                    previous_review[0].delete()
                data = form.save(commit=False)
                # Because it's a model form, we just need to massage these implicit
                # fields and can just save the new object directly
                data.reviewer = request.user
                data.noodle = noodle
                data.save()
                messages.add_message(request, messages.SUCCESS, "Review added successfully")
                # Create new ReviewImage after review is created to prevent issues
                if request.FILES:
                    file = list(request.FILES.keys())[0]
                    image = request.FILES[file]
                    review_image = ReviewImage(image = image, review = data, uploader = request.user)
                    review_image.save()
                # Call action hook to save user stats
                if not previous_review:
                    request.user.profile.increment_meta_val("Reviewed", 1)
                    dispatch_hook(request.user, "review-created", count=request.user.profile.get_meta_val("Reviewed"))

    return HttpResponseRedirect(reverse('noodle', kwargs={"noodle_id" : noodle.id}))
