from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from rameniaapp.decorators import user_is_moderator

@login_required(login_url="/app/login")
@user_is_moderator
def view_mod_page(request):
    '''Basic utilitarian page to provide links to moderator views'''
    return render(request, 'moderator.html')