from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from rameniaapp.forms import EditRamenForm
from rameniaapp.models import Noodle, NoodleImage, Edit, Tag
from .edit_util import apply_change

def ramen_edit_view(request, noodle_id):
  noodle = Noodle.objects.get(pk=noodle_id)
  # If this is a POST request then process the Form data
  if request.method == 'POST':
    user = request.user
      # Create a form instance and populate it with data from the request of the user
    form = EditRamenForm(request.POST or None, request.FILES)
    # Check if the form is valid:
    if form.is_valid():
        print(form.cleaned_data)
      # Helps with clean format
        metadata = { "Name": form.cleaned_data["name"], "Description": form.cleaned_data["description"], \
              "Flavor": form.cleaned_data["flavor"], \
              "Manufacturer": form.cleaned_data["manufacturer"], \
              "Released": form.cleaned_data["released"], "Line": form.cleaned_data["line"] }
        edit = Edit(editor = user, change = metadata, noodle = noodle)
        if request.FILES:
                file = list(request.FILES.keys())[0]
                edit.image = request.FILES[file] 
        edit.save()
        apply_change(edit) 
        # form.save()
        # redirect to a new URL:
        return HttpResponseRedirect('/app/')
  else:
    initial = {"name": noodle.name, "description": noodle.metadata["Description"], \
              "flavor": noodle.metadata["Flavor"], \
              "manufacturer": noodle.metadata["Manufacturer"], \
              "released": noodle.metadata["Released"], "line": noodle.metadata["Line"]}
    form = EditRamenForm(initial = initial)
    template = loader.get_template('edit_ramen.html')
    context = {
        'form': form, 'noodle' : noodle
    }
  return HttpResponse(template.render(context, request))
  #return render(request, "add_ramen.html",{"form":form})

  