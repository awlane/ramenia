from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from rameniaapp.forms import RamenForm
from rameniaapp.models import Noodle, NoodleImage, Edit, Tag
from .edit_util import apply_change

def ramen_create_view(request):
  form = RamenForm()
  # If this is a POST request then process the Form data
  if request.method == 'POST':
    user = request.user
      # Create a form instance and populate it with data from the request of the user
    form = RamenForm(request.POST or None, request.FILES)
    # Check if the form is valid:
    if form.is_valid():
        print(form.cleaned_data)
      # Helps with clean format
        metadata = { "Name": form.cleaned_data["name"], "Description": form.cleaned_data["description"], \
              "Flavor": form.cleaned_data["flavor"], \
              "Manufacturer": form.cleaned_data["manufacturer"], \
              "Released": form.cleaned_data["released"], "Line": form.cleaned_data["line"] }
        edit = Edit(editor = user, change = metadata)
        edit.save()
        apply_change(edit) 
        # form.save()
        # redirect to a new URL:
        return HttpResponseRedirect('/app/')
#  else:
#      form = Add_Ramen_Form()
  #    description.error(request,"Input could not be saved")
    #   return HttpResponseRedirect("add_ramen.html")
  
  template = loader.get_template('add_ramen.html')
  context = {
      'form': form,
  }
  return HttpResponse(template.render(context, request))
  #return render(request, "add_ramen.html",{"form":form})

  