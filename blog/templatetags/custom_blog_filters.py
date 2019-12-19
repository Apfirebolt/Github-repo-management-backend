from django import template

register = template.Library()

@register.filter
def capitalText(value):
    return value.upper()