#!/usr/bin/env python

""" Utility module to hold useful methods for the swear jar application. """

__author__ = "Ian Adam Naval"
__copyright__ = "Copyright 2012 Ian Adam Naval"

__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Ian Adam Naval"
__email__ = "ianonavy@gmail.com"
__status__ = "Development"
__date__ = "11 January 2012"


def load_page(request, template, extra={}):
    """Special page rendering function for bookstore application pages.

    Args::
    request: the original page request passed to the view
    template: the filename of the template to load
    extra: a dictionary holding extra information to inject into the
        template's context in addition to the user's model and
        role (default empty dictionary)

    """
    return render_to_response('core/%s' % template, dict(extra.items()),
        context_instance=RequestContext(request))


def message_page(request, message, back=""):
    """Shortcut function to return a simple message page."""
    extra = {'message': message, 'back': back}
    return load_page(request, 'message.html', extra)


def error_page(request, error):
    """Shortcut function to return a error message page."""
    extra = {'error': error}
    return load_page(request, 'error.html', extra)


def get_remote_ip(request):
    try:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    except:
        ip = request.META['REMOTE_ADDR']
    return ip[ip.find(" ")+1:]
