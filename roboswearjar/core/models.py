#!/usr/bin/env python

""" Django models file to define the models for the swear jar application.

Contains code to encapsulate a swear type, a particular swear, and an
individual RoboKnights team member.

"""

from django.db import models

__author__ = "Ian Adam Naval"
__copyright__ = "Copyright 2012 Ian Adam Naval"

__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Ian Adam Naval"
__email__ = "ianonavy@gmail.com"
__status__ = "Development"
__date__ = "11 January 2012"


class Knight(models.Model):
    """ Model that encapsulates a specific member of Team RoboKnights (e.g. a
    Knight). A Knight has many swears."""

    name = models.CharField(max_length=255)

    def debt_for_type(self, swear_type):
        """ Returns the debt for a particular type of swear. """

        debt = 0
        for swear in Swear.objects.filter(speaker=self, swear_type=swear_type):
            debt = debt + swear.getValue()
        return debt

    def all_debts(self):
        """ Returns an array with all the debt of the knight. """

        class Debt:
            type = None
            count = 0
            value = 0

        all_debts = []
        for swear_type in SwearType.objects.all():
            debt = Debt()
            debt.type = swear_type
            debt.value = self.debt_for_type(swear_type)
            if debt.value != 0 and debt.type.value != 0:
                debt.count = debt.value / debt.type.value
                all_debts.append(debt)
        return all_debts

    def total_debt(self):
        """ Returns the total debt for all types of swears. """

        debt = 0
        for swear in Swear.objects.filter(speaker=self):
            debt = debt + swear.getValue()
        return debt

    def add_swear(self, swear_type):
        """ Adds a new swear to the database with this Knight as its
        speaker. """

        swear = Swear()
        swear.sweartype = swear_type
        swear.speaker = self
        swear.save()

    def __unicode__(self):
        return self.name


class SwearType(models.Model):
    """ Model that encapsulates a particular swear type. Instances of these are
    meant to be created in the Django Administration page."""

    phrase = models.CharField(max_length=255)
    value = models.FloatField()

    def __unicode__(self):
        return self.phrase


class Swear(models.Model):
    """ Model that encapsulates a specific instance of a swear. These are 
    generated and saved to the database by the a Knight's add_swear method. A
    Swear has one type and one speaker. """

    swear_type = models.ForeignKey(SwearType)
    speaker = models.ForeignKey(Knight)

    def getValue(self):
        return self.swear_type.value

    def __unicode__(self):
        return "%s said %s." % (self.speaker, self.swear_type)
