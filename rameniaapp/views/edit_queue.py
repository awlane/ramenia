from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from rameniaapp.models import Noodle, Edit
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .edit_util import apply_change
from django.contrib.auth.decorators import login_required


class EditsList(LoginRequiredMixin, ListView):
    model = Edit
    context_object_name = "edits"
    template_name = "edits_view.html"
    login_url="/app/login"

    def get_queryset(self):
        if "noodle_id" in self.kwargs:
            noodle = get_object_or_404(Noodle, pk=self.kwargs["noodle_id"])
            return Edit.objects.filter(noodle=noodle)
        elif "new" in self.kwargs:
            return Edit.objects.filter(noodle=None)
        elif "user_id" in self.kwargs:
            user = get_object_or_404(User, pk=self.kwargs["user_id"])
            return Edit.objects.filter(editor=user)
        else:
            return Edit.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["MEDIA_URL"] = settings.MEDIA_URL
        return context

@login_required(login_url="/app/login")
def apply_edit(request, edit_id):
    if request.method == "POST":
        edit = Edit.objects.get(pk=edit_id)
        apply_change(edit)
        return HttpResponseRedirect(request.path)
    else:
        return HttpResponseRedirect("/app/mod/edits")


@login_required(login_url="/app/login")
def reject_edit(request, edit_id):
    if request.method == "POST":
        edit = Edit.objects.get(pk=edit_id).delete()
        return HttpResponseRedirect(request.path)
    else:
        return HttpResponseRedirect("/app/mod/edits")