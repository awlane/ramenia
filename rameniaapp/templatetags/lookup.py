#Code based on Stack Exchange answers from Yuji Tomita https://stackoverflow.com/a/8000078/9627903
from django import template
register = template.Library()
@register.filter(name='lookup')
def lookup(dictionary, key):
    '''Do dictionary lookup for template (not possible normally)'''
    return dictionary.get(key)
