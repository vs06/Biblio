#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import redirect

# Create your views here.

def index(request):
    return redirect('/admin/')