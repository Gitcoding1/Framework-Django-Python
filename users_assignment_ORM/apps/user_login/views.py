# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from models import *

# Create your views here.

#  /// root route //
def index(request):
    context ={
        'users': User.objects.all()
    }
    return render(request,'user_login_html/index.html',context)
