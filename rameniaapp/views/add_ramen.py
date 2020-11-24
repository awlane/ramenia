from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from rameniaapp.forms import AddNoodleForm
from rameniaapp.models import Noodle, NoodleImage, Edit, Tag
from .edit_util import apply_change
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url="/app/login")
def ramen_create_view(request):
    '''View for handling add noodle form'''
    form = AddNoodleForm()
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        user = request.user
        # Create a form instance and populate it with data from the request of the user
        form = AddNoodleForm(request.POST or None, request.FILES)
        # Check if the form is valid:
        if form.is_valid():
            print(form.cleaned_data)
            # Helps with clean format
            metadata = { "Name": form.cleaned_data["name"], "Description": form.cleaned_data["description"], \
                        "Flavor": form.cleaned_data["flavor"], \
                        "Manufacturer": form.cleaned_data["manufacturer"], \
                        "Released": form.cleaned_data["released"], "Line": form.cleaned_data["line"], \
                        "Tags": form.cleaned_data["tags"] }
            edit = Edit(editor = user, change = metadata)
            # Standard code to get file from request and set as edit's image
            if request.FILES:
                file = list(request.FILES.keys())[0]
                edit.image = request.FILES[file]
            edit.save()
            messages.add_message(request, messages.SUCCESS, "Entry submitted successfully- please wait for moderator approval")
            # redirect to a new URL:
            return HttpResponseRedirect('/app/')
    else:
        template = loader.get_template('add_ramen.html')
        context = {
            'form': form,
        }
        return HttpResponse(template.render(context, request))

