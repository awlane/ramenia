from django import template
from rameniaapp.models import NoodleReport, ProfileReport, ReviewReport

register = template.Library()
@register.filter(name='get_creator')
def get_creator(obj):
    '''Get the creator of a report in template'''
    if type(obj) == NoodleReport:
        if obj.noodle.editor:
            return obj.noodle.editor.id
    elif type(obj) == ProfileReport:
        if obj.profile.user:
            return obj.profile.user.id
    elif type(obj) == ReviewReport:
        if obj.review.reviewer:
            return obj.review.reviewer.id
    return None