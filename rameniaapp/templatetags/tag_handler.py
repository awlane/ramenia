from django import template

register = template.Library()
@register.filter(name='tag_value_list')
def tag_value_list(obj):
    '''Returns a list of all tag names associated with a noodle'''
    return obj.values_list("name", flat=True)

@register.filter(name='list2string')
def list2string(list_obj):
    '''Converts list to string efficiently'''
    return ", ".join(list_obj)

@register.filter(name='list_equality')
def list_equality(value_a, value_b):
    '''Casting to set allows to check equality by value'''
    return set(value_a) == set(value_b)
