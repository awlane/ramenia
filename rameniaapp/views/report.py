from django.shortcuts import render, HttpResponse
from django.template import loader
from django.conf import settings
from rameniaapp.models import ReviewReport, ProfileReport, NoodleReport, Report, Review, Profile, Noodle
from django.views.generic import ListView

class ReportList(ListView):
    model = Report
    context_object_name = "reports"
    template_name = "report.html"
    def get_queryset(self):
        print(self.kwargs)
        if "item_id" in self.kwargs:
            item_tuple = self.get_item(self.kwargs["item_id"])
            self.kwargs[item_tuple[0]] = item_tuple[1]
            del self.kwargs["item_id"]
        return self.model.objects.filter(**self.kwargs)

    def get_item(self, id):
        '''Returns a tuple containing the key name and item'''
        return (None, None)

class NoodleReportList(ReportList):
    model = NoodleReport
    def get_item(self, id):
        '''Returns a tuple containing the key name and item'''
        noodle = Noodle.objects.get(id=id)
        return ("noodle", noodle)

class ReviewReportList(ReportList):
    model = ReviewReport
    def get_item(self, id):
        '''Returns a tuple containing the key name and item'''
        review = review.objects.get(id=id)
        return ("review", review)

class ProfileReportList(ReportList):
    model = ProfileReport
    def get_item(self, id):
        '''Returns a tuple containing the key name and item'''
        profile = Profile.objects.get(id=id)
        return ("profile", profile)

def view_reports_disam(request):
    return render(request, 'report_disam.html')