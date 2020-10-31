from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from rameniaapp.forms import EditNoodleForm
from rameniaapp.models import Noodle, NoodleImage, Edit, Tag
from .edit_util import apply_change
from django.contrib.auth.decorators import login_required

@login_required(login_url="/app/login")
def ramen_edit_view(request, noodle_id):
    noodle = Noodle.objects.get(pk=noodle_id)
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        user = request.user
        # Create a form instance and populate it with data from the request of the user
        form = EditNoodleForm(request.POST or None, request.FILES)
        # Check if the form is valid:
        if form.is_valid():
            print(form.cleaned_data)
            # Helps with clean format
            metadata = { "Name": form.cleaned_data["name"], "Description": form.cleaned_data["description"], \
                        "Flavor": form.cleaned_data["flavor"], \
                        "Manufacturer": form.cleaned_data["manufacturer"], \
                        "Released": form.cleaned_data["released"], "Line": form.cleaned_data["line"], \
                        "Tags": form.cleaned_data["tags"]  }
            edit = Edit(editor = user, change = metadata, noodle = noodle)
            if request.FILES:
                file = list(request.FILES.keys())[0]
                edit.image = request.FILES[file]
            edit.save()
            apply_change(edit)
        return HttpResponseRedirect('/app/')
    else:
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