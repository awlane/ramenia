from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.contrib.auth.models import User
from rameniaapp.models import ReviewReport, ProfileReport, NoodleReport, Report, Review, Profile, Noodle
from django.views.generic import ListView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from rameniaapp.decorators import user_is_moderator
from rameniaapp.actionhookutils import dispatch_hook
from rameniaapp.utils import UserIsModeratorMixin
from django.forms.widgets import Select
from django.contrib import messages

class ReportForm(LoginRequiredMixin, CreateView):
    '''Class based view for creating reports'''
    template_name = "report_form.html"
    model = Report
    success_url = "/app"
    fields = ["reason"]
    url_path = "/app"
    login_url="/app/login"

    def get_form(self, form_class=None):
        form = super(ReportForm, self).get_form(form_class)
        form.fields['reason'].widget.attrs.update({'class':'form-control'})
        return form

    def form_valid(self, form):
        '''Ensures hidden form values are filled'''
        form.instance.reporter = self.request.user
        form.instance.status = 'OP'
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        '''Adds url_path value and relevant object id to template'''
        context = super().get_context_data(**kwargs)
        context["id"] = self.kwargs["id"]
        context["url_path"] = self.url_path
        return context

class NoodleReportForm(ReportForm):
    '''Class based view for reporting noodles'''
    model = NoodleReport
    #This is used to allow the form to create the correct object
    url_path = "noodle_report"

    def form_valid(self, form):
        '''Ensures hidden form values are filled'''
        form.instance.noodle = Noodle.objects.get(pk=self.kwargs["id"])
        form.instance.type = 'ND'
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        '''Passes item name to template'''
        context = super().get_context_data(**kwargs)
        context["name"] = Noodle.objects.get(pk=self.kwargs["id"]).name
        return context

class ReviewReportForm(ReportForm):
    '''Class based view for reporting reviews'''
    model = ReviewReport
    url_path = "review_report"

    def form_valid(self, form):
        '''Ensures hidden form values are filled'''
        form.instance.review = Review.objects.get(pk=self.kwargs["id"])
        form.instance.type = 'RV'
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        '''Passes item name to template'''
        context = super().get_context_data(**kwargs)
        context["name"] = Review.objects.get(pk=self.kwargs["id"]).title
        return context

class ProfileReportForm(ReportForm):
    '''Class based view for reporting profile'''
    model = ProfileReport
    url_path = "profile_report"

    def form_valid(self, form):
        '''Ensures hidden form values are filled'''
        form.instance.profile = Profile.objects.get(pk=self.kwargs["id"])
        form.instance.type = 'PF'
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        '''Passes item name to template'''
        context = super().get_context_data(**kwargs)
        context["name"] = Profile.objects.get(pk=self.kwargs["id"]).name
        return context

class ReportList(LoginRequiredMixin, UserIsModeratorMixin, ListView):
    '''Class based view for viewing reports'''
    # These values are overriden for the subclasses so we can create
    # multiple types of noodles without rewriting code
    model = Report
    item_type = ""
    context_object_name = "reports"
    template_name = "report_view.html"
    login_url="/app/login"

    def get_queryset(self):
        '''Get all reports for specific objects'''
        if "item_id" in self.kwargs:
            item_tuple = self.get_item(self.kwargs["item_id"])
            self.kwargs[item_tuple[0]] = item_tuple[1]
            # This prevents the next line from breaking
            del self.kwargs["item_id"]
        # Using get_item, this lets us filter for any kind of object without
        # writing extra code
        return self.model.objects.filter(**self.kwargs)

    def get_item(self, id):
        '''Returns a tuple containing the key name and item'''
        return (None, None)

    def get_context_data(self, **kwargs):
        '''Knowing the item type lets us not break things'''
        context = super().get_context_data(**kwargs)
        context['item_type'] = self.item_type
        return context

class NoodleReportList(ReportList):
    '''List of noodle reports'''
    model = NoodleReport
    item_type = "Noodles"

    def get_item(self, id):
        '''Returns a tuple containing the key name and item'''
        noodle = Noodle.objects.get(id=id)
        return ("noodle", noodle)

class ReviewReportList(ReportList):
    '''List of review reports'''
    model = ReviewReport
    item_type = "Reviews"

    def get_item(self, id):
        '''Returns a tuple containing the key name and item'''
        review = Review.objects.get(id=id)
        return ("review", review)

class ProfileReportList(ReportList):
    '''List of profile reports'''
    model = ProfileReport
    item_type = "Profiles"

    def get_item(self, id):
        '''Returns a tuple containing the key name and item'''
        profile = Profile.objects.get(id=id)
        return ("profile", profile)

@login_required(login_url="/app/login")
@user_is_moderator
def ban_user(request, report_type, user_id):
    '''Ban a user by their id; expects report_type arg for redirect reasons'''
    if request.method == "POST":
        user = User.objects.get(pk=user_id).delete()
        path = None
        if report_type == "ND":
            path = "reports/noodle"
        elif report_type == "RV":
            path = "reports/review"
        elif report_type == "PF":
            path = "reports/profile"
        messages.add_message(request, messages.WARNING, "User banned")
        return HttpResponseRedirect("/app/mod/{}".format(path))
    else:
        return HttpResponseRedirect("/app/mod")

@login_required(login_url="/app/login")
@user_is_moderator
def delete_content(request, report_id):
    '''This method deletes offending items that have been reported, or just their content'''
    if request.method == "POST":
        report = Report.objects.get(pk=report_id)
        reporter = report.reporter
        creator = None
        path = get_return_path(report)
        # Deleting object is dependent on type
        if report.type == "RV":
            report = ReviewReport.objects.get(pk=report_id)
            creator = report.review.reviewer
            report.review.delete()
        elif report.type == "ND":
            report = NoodleReport.objects.get(pk=report_id)
            creator = report.noodle.editor
            report.noodle.delete()
        elif report.type == "PF":
            # Deleting a profile will break fundamental assumptions, so we instead
            # remove all content from it.
            report = ProfileReport.objects.get(pk=report_id)
            report.profile.name = "AnonymousUser"
            report.profile.profile_pic = Profile._meta.get_field('profile_pic').default
            report.profile.metadata["Description"] = ""
            report.profile.save()
            creator = report.profile.user
            report.delete()
        # If we delete the content, it was reasonable to report it
        dispatch_hook(reporter, "good-report")
        if creator:
            # If the noodle's creator hasn't been banned, penalize them
            dispatch_hook(creator, "bad-content")
        messages.add_message(request, messages.WARNING, "Content deleted")
        return HttpResponseRedirect("/app/mod/reports/{}".format(path))
    else:
        return HttpResponseRedirect("/app/mod")

@login_required(login_url="/app/login")
@user_is_moderator
def update_report_status(request, report_id, status):
    '''Change report status to "open", "resolved", or "spam"'''
    if request.method == "POST":
        # Validate status is the correct value
        if status in dict(Report.STATUS_CHOICES):
            report = Report.objects.get(pk=report_id)
            report.status = status
            report.save()
            creator = None
            path = get_return_path(report)
            # Get the creator of the relevant object/report
            if report.type == "RV":
                report = ReviewReport.objects.get(pk=report_id)
                creator = report.review.reviewer
            elif report.type == "ND":
                report = NoodleReport.objects.get(pk=report_id)
                creator = report.noodle.editor
            elif report.type == "PF":
                report = ProfileReport.objects.get(pk=report_id)
                creator = report.profile.user
            # Reward people for good reports
            if status == "ED":
                if report.reporter:
                    dispatch_hook(report.reporter, "good-report")
                if creator:
                    dispatch_hook(creator, "bad-content")
                messages.add_message(request, messages.SUCCESS, "Report marked as resolved")
            # Penalize people for bad reports
            if status == "SP":
                if report.reporter:
                    dispatch_hook(report.reporter, "bad-report")
                messages.add_message(request, messages.WARNING, "Report marked as spam")
        return HttpResponseRedirect("/app/mod/reports/{}".format(path))
    else:
        return HttpResponseRedirect("/app/mod")

@login_required(login_url="/app/login")
@user_is_moderator
def ignore_report(request, report_id):
    '''Ignore (delete) a report'''
    if request.method == "POST":
        report = Report.objects.get(pk=report_id)
        path = get_return_path(report)
        if report.reporter:
            # We assume a bad report is worth deleting if its creator
            # wasn't banned
            dispatch_hook(report.reporter, "bad-report")
        report.delete()
        messages.add_message(request, messages.WARNING, "Report ignored")
        return HttpResponseRedirect("/app/mod/reports/{}".format(path))
    else:
        return HttpResponseRedirect("/app/mod")


def get_return_path(report):
    '''Util method to return a correct redirect path'''
    if report.type == "RV":
        return "review"
    elif report.type == "ND":
        return "noodle"
    elif report.type == "PF":
        return "profile"