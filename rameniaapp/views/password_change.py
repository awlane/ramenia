from django.shortcuts import render, HttpResponseRedirect
from rameniaapp.forms import ChangePasswordForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="/app/login")
def change_password(request):
    '''View to handle change password form'''
    # This is very boilerplate as we use the stock logic,
    # majority of heavy lifting is in the base form we
    # inherited
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Password updated successfully")
            return HttpResponseRedirect('/app/')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'password_change.html', {"form": form})
