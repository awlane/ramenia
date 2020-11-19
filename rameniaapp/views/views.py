from django.shortcuts import render, HttpResponse
from django.contrib import messages
import random

from rameniaapp.decorators import user_is_moderator

def index(request):
    '''Homepage view'''
    return render(request, 'index.html')


