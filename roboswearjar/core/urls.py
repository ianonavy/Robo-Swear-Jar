#!/usr/bin/env python
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('core.views',
    url(r'^$', 'index'),
    url(r'^login/$', 'login_'),
    url(r'^logout/$', 'logout_'),
    url(r'^add_knight/$', 'add_knight'),
    url(r'^add_swear/$', 'add_swear'),
)
