#!/usr/bin/env python

"""Django views for the swear jar application."""

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

    knights = Knight.objects.all()
    types = SwearType.objects.all()
    
    total = 0
    for knight in knights:
        total = total + knight.total_debt()
    
    load_page("index.html", {
        "knights": knights
        "types": types
        "total": total
        })

    load_page("guests.html")


def login(request):
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
            HttpResponseRedirect('/?invalid=true')
    
    HttpResponseRedirect('/')


def add_knight(request):
    """ View that handles creating a new RoboKnights team member. """

    if request.method == "POST":
        new_member = Knight()
        new_member.name = request.POST["name"]
        new_member.save()

def add_swear(request):
    """ View that adds a new swear record for a team member. """
