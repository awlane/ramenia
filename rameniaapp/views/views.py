from django.shortcuts import render, HttpResponse
from django.contrib import messages

# Create your views here.
def index(request):
    messages.add_message(request, messages.SUCCESS, 'Hello world.')
    return render(request, 'index.html')


