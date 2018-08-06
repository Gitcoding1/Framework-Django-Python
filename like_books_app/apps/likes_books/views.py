# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from models import *

# Create your views here.
def index(request):
    context = {
        'users': User.objects.all(),
        'books': Book.objects.all(),
    }
    return render(request,'index.html',context=context)
