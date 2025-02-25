from django import template

register = template.Library()
@register.filter(name='is_mod')
def is_mod(obj):
    '''Boolean check for if user is moderator'''
    return obj.groups.filter(name="moderator").exists()
