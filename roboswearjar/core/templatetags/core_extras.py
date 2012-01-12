#!/usr/bin/env python

""" Extra custom template tags for use in the swear jar. """

from django import template
import locale
locale.setlocale(locale.LC_ALL, '')
register = template.Library()

 
@register.filter()
def currency(value):
    return locale.currency(value, grouping=True)
