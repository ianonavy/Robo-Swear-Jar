#!/usr/bin/env python

"""Django views for the swear jar application."""

from urllib import unquote_plus
from django.contrib.auth import logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from utils import load_page
from models import Knight, SwearType, Swear

__author__ = "Ian Adam Naval"
__copyright__ = "Copyright 2012 Ian Adam Naval"

__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Ian Adam Naval"
__email__ = "ianonavy@gmail.com"
__status__ = "Development"
__date__ = "11 January 2012"

def index(request):
    """ View that handles displaying the home page. """

    if request.user.is_authenticated():

        knights = Knight.objects.all().order_by('name')
        types = SwearType.objects.all()
        
        total = 0
        for knight in knights:
            total = total + knight.total_debt()
    
        return load_page(request, "index.html", {
            "knights": knights,
            "types": types,
            "total": total })

    else:
        return load_page(request, "guests.html")


def login_(request):
    """ View that handles logging in. """

    if request.method == "POST":
        # Get login information from the POST data.
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user.
        user = authenticate(username=username, password=password)
        
        # Display the correct template.
        if user is not None:
            login(request, user)
        else:
            return HttpResponseRedirect('/?invalid=true')
    
    return HttpResponseRedirect('/')


def logout_(request):
    """ View that handles logging out """

    logout(request)
    return HttpResponseRedirect('/')


def add_knight(request):
    """ View that handles creating a new RoboKnights team member. """

    if request.method == "POST":
        new_member = Knight()
        new_member.name = request.POST.get('name')
        new_member.save()

    return HttpResponseRedirect('/')


def add_swear(request):
    """ View that adds a new swear record for a team member. """

    if request.method == "GET":
        # POST is better, but GET can be used in anchor tag.

        type_ = request.GET.get('type')
        id_ = request.GET.get('id')

        swear_type = SwearType.objects.get(id=type_)
        speaker = Knight.objects.get(id=id_)

        new_swear = Swear()
        new_swear.swear_type = swear_type
        new_swear.speaker = speaker
        new_swear.save()
        
    return HttpResponseRedirect('/')


def add_type(request):
    """ View that adds a new swewar type. """

    if request.method == "POST":
        phrase = unquote_plus(request.POST.get('phrase'))
        valuey = request.POST.get('value')

        new_type = SwearType()
        new_type.phrase = phrase
        new_type.value = float(value)
        new_type.save()

    return HttpResponseRedirect('/')


def undo(request):
    """ View that destroys the last created swear. """

    try:
        latest = Swear.objects.all().latest('id')
        latest.delete()
    except:
        pass

    return HttpResponseRedirect('/')
