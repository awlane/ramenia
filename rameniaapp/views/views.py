from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')


