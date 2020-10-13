from django.shortcuts import render, HttpResponse
from django.template import loader
from django.conf import settings
from rameniaapp.forms import AddRamenForm
from rameniaapp.models import AddRamen

def ramen_create_view(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = Add_Ramen_Form(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            manufacturer = form.cleaned_data['manufacturer']
            description = form.cleaned_data['description']
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('index')
    else:
        descritpion.error(request,'Input could not be saved')
        return HttpResponseRedirect('index')

    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))