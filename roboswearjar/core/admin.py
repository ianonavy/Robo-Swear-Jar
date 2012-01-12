#!/usr/bin/env python

"""Django admin configuration form.

Contains classes to configure how the models are displayed and edited in the
Django administration side.

"""

from django.contrib import admin
from core.models import Knight, SwearType, Swear


__author__ = "Ian Adam Naval"
__copyright__ = "Copyright 2011 Ian Adam Naval"

__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Ian Adam Naval"
__email__ = "ianonavy@gmail.com"
__status__ = "Development"
__date__ = "11 January 2012"


class KnightAdmin(admin.ModelAdmin):
    """Admin form configuration for the Knight model."""

    fieldsets = [
        ('Knight', {'fields': [
            'name'
        ]})
    ]
    list_display = ('id', 'name')


class SwearTypeAdmin(admin.ModelAdmin):
    """Admin form configuration for the SwearType model."""

    fieldsets = [
        ('Swear Type', {'fields': [
            'phrase',
            'value',
        ]})
    ]
    list_display = ('id', 'phrase', 'value')


class SwearAdmin(admin.ModelAdmin):
    """Admin form configuration for the Swear model."""

    fieldsets = [
        ('Swear', {'fields': [
            'speaker',
            'swear_type',
        ]})
    ]
    list_display = ('speaker', 'swear_type')


# Register the admin forms.
admin.site.register(Knight, KnightAdmin)
admin.site.register(SwearType, SwearTypeAdmin)
admin.site.register(Swear, SwearAdmin)
