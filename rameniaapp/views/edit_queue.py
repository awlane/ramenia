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
from rameniaapp.actionhookutils import dispatch_hook
from rameniaapp.decorators import user_is_moderator
from rameniaapp.utils import UserIsModeratorMixin
from django.contrib import messages

class EditsList(LoginRequiredMixin, UserIsModeratorMixin, ListView):
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
@user_is_moderator
def apply_edit(request, edit_id):
    if request.method == "POST":
        edit = Edit.objects.get(pk=edit_id)
        apply_change(edit)

        # call hook
        if edit.noodle:
            edit.editor.profile.increment_meta_val("Noodle Edits", 1)
            dispatch_hook(edit.editor, "noodle-edited", count=edit.editor.profile.metadata["Noodle Edits"])
        else:
            edit.editor.profile.increment_meta_val("Entries Made", 1)
            dispatch_hook(edit.editor, "noodle-added", count=edit.editor.profile.metadata["Entries Made"])
        dispatch_hook(edit.editor, "good-content")
        messages.add_message(request, messages.SUCCESS, "Noodle changes approved")
        return HttpResponseRedirect(request.path)
    else:
        return HttpResponseRedirect("/app/mod/edits")


@login_required(login_url="/app/login")
@user_is_moderator
def reject_edit(request, edit_id):
    if request.method == "POST":
        edit = Edit.objects.get(pk=edit_id).delete()
        messages.add_message(request, messages.WARNING, "Noodle changes rejected")
        return HttpResponseRedirect(request.path)
    else:
        return HttpResponseRedirect("/app/mod/edits")
