from django.shortcuts import render, HttpResponse
from django.template import loader
from django.conf import settings
from rameniaapp.forms import AddRamenForm
from rameniaapp.models import Ramen

def ramen_create_view(request):
    form = AddRamenForm()
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request of the user
        form = AddRamenForm(request.POST or None, request.FILES)
        # Check if the form is valid:
        if form.is_valid():
          # Helps with clean format
            name = form.cleaned_data["name"]
            manufacturer = form.cleaned_data["manufacturer"]
            description = form.cleaned_data["description"]
            form.save()
            # redirect to a new URL:
            form = AddRamenForm()
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

  