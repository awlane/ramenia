from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url="/app/login")
def view_mod_page(request):
    return render(request, 'moderator.html')