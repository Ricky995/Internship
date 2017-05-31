# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    date=datetime.datetime.now()
    return HttpResponse("The time is %s" % date)
# Create your views here.
