# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from models import *
# Create your views here.
def index(request):
    context = {
        'books' : Book.objects.all(),
        'authors': Author.objects.all()
    }
    return render(request, 'books_authors/index.html',context)