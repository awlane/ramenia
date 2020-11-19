from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from rameniaapp.forms import EditNoodleForm
from rameniaapp.models import Noodle, NoodleImage, Edit, Tag
from .edit_util import apply_change
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages


@login_required(login_url="/app/login")
def ramen_edit_view(request, noodle_id):
    '''View for handling edit noodle form'''
    noodle = Noodle.objects.get(pk=noodle_id)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        user = request.user
        # Create a form instance and populate it with data from the request of the user
        form = EditNoodleForm(request.POST or None, request.FILES)
        # Check if the form is valid
        if form.is_valid():
            # There's not a clean looking way to turn form data into JSON
            # unfortunately
            metadata = { "Name": form.cleaned_data["name"], "Description": form.cleaned_data["description"], \
                        "Flavor": form.cleaned_data["flavor"], \
                        "Manufacturer": form.cleaned_data["manufacturer"], \
                        "Released": form.cleaned_data["released"], "Line": form.cleaned_data["line"], \
                        "Tags": form.cleaned_data["tags"]  }
            # Create Edit object and associate image if added
            edit = Edit(editor = user, change = metadata, noodle = noodle)
            if request.FILES:
                file = list(request.FILES.keys())[0]
                edit.image = request.FILES[file]
            edit.save()
        messages.add_message(request, messages.SUCCESS, "Edit submitted successfully- please wait for moderator approval")

            #apply_change(edit)
        return HttpResponseRedirect(reverse('noodle', kwargs={"noodle_id" : noodle.id}))
    else:
        # Prepopulate initial values for edit form- otherwise it's not a very good
        # edit form
        # Yes this is the best way to turn the tags into a string, I do not
        # like it either
        tags = ",".join(noodle.tags.values_list("name", flat=True))
        initial = {"name": noodle.name, "description": noodle.metadata["Description"], \
                    "flavor": noodle.metadata["Flavor"], \
                    "manufacturer": noodle.metadata["Manufacturer"], \
                    "released": noodle.metadata["Released"], "line": noodle.metadata["Line"], \
                    "tags": tags}
        form = EditNoodleForm(initial = initial)
        template = loader.get_template('edit_ramen.html')
        context = {
            'form': form, 'noodle' : noodle
        }
        return HttpResponse(template.render(context, request))