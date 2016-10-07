#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    #url(r'^$', include('biblio2.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
]
