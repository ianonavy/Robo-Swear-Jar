#!/usr/bin/env python

"""Django views for the swear jar application."""

from django.contrib.auth import logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.views import login
from utils import load_page
from models import Knight, SwearType

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
        new_member.name = request.POST["name"]
        new_member.save()

    return HttpResponseRedirect('/')


def add_swear(request):
    """ View that adds a new swear record for a team member. """

    if request.method == "GET":
        # POST is better, but GET can be used in anchor tag.

        type_ = request.GET.get('type')
        id_ = request.GET.get('id')

        swear_type = SwearType.objects.filter(id=type_)
        speaker = Knight.objects.filter(id=id_)
        
    return HttpResponseRedirect('/')
