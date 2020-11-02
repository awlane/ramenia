from django import template

register = template.Library()
@register.filter(name='tag_value_list')
def tag_value_list(obj):
    return obj.values_list("name", flat=True)

@register.filter(name='list2string')
def list2string(list_obj):
    return ", ".join(list_obj)

@register.filter(name='list_equality')
def list_equality(value_a, value_b):
    return set(value_a) == set(value_b)
