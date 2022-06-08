from django import template

register = template.Library()

def range_filter(value):
    return value[0:600] + "............click read more to read full article"



register.filter('range_filter',range_filter)
