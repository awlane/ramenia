from django.shortcuts import render, HttpResponse
from django.template import loader
from django.conf import settings
from rameniaapp.models import ReviewReport, ProfileReport, NoodleReport, Report, Review, Profile, Noodle
from django.views.generic import ListView

#TODO: Needs permissions added once that is set up
class ReportList(ListView):
    model = Report
    context_object_name = "reports"
    template_name = "report.html"
    item_type = ""

    def get_queryset(self):
        if "item_id" in self.kwargs:
            item_tuple = self.get_item(self.kwargs["item_id"])
            self.kwargs[item_tuple[0]] = item_tuple[1]
            del self.kwargs["item_id"]
        return self.model.objects.filter(**self.kwargs)

    def get_item(self, id):
        '''Returns a tuple containing the key name and item'''
        return (None, None)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['item_type'] = self.item_type
        return context

class NoodleReportList(ReportList):
    model = NoodleReport
    item_type = "Noodles"

    def get_item(self, id):
        '''Returns a tuple containing the key name and item'''
        noodle = Noodle.objects.get(id=id)
        return ("noodle", noodle)

class ReviewReportList(ReportList):
    model = ReviewReport
    item_type = "Reviews"

    def get_item(self, id):
        '''Returns a tuple containing the key name and item'''
        review = review.objects.get(id=id)
        return ("review", review)

class ProfileReportList(ReportList):
    model = ProfileReport
    item_type = "Profiles"

    def get_item(self, id):
        '''Returns a tuple containing the key name and item'''
        profile = Profile.objects.get(id=id)
        return ("profile", profile)

def view_reports_disam(request):
    return render(request, 'report_disam.html')