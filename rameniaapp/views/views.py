from django.shortcuts import render, HttpResponse

from rameniaapp.decorators import user_is_moderator

# Create your views here.
def index(request):
    return render(request, 'index.html')


