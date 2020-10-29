from django.shortcuts import render, HttpResponse
from django.template import loader
from django.conf import settings
from rameniaapp.models import Noodle, Edit
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class EditsList(ListView):
    model = Edit
    context_object_name = "edits"
    template_name = "edits_view.html"

    def get_queryset(self):
        if "noodle_id" in self.kwargs:
            if not self.kwargs["noodle_id"] == None:
                noodle = get_object_or_404(Noodle, pk=self.kwargs["noodle_id"])
                return Edit.objects.filter(noodle=noodle)
            else:
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