from django.shortcuts import render, HttpResponse
from django.template import loader
from django.conf import settings
from rameniaapp.models import Report

def view_reports(request):
    reports = Report.objects.all()
    template = loader.get_template('report.html')
    context = { "reports" : reports }
    return HttpResponse(template.render(context, request))

def filter_reports(request, report_type):
    reports = Report.objects.get(type=report_type)
    template = loader.get_template('report.html')
    context = { "reports" : reports }
    return HttpResponse(template.render(context, request))