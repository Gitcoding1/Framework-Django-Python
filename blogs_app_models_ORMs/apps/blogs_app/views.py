# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, HttpResponse, redirect
from .models import Blog

# Create your views here.
def index(request):
    context= {
        "users": Blog.objects.all()
    }
    return render(request,'blogs_app_html/index.html',context)


def update(request):
    errors = Blog.objects.basic_validator(request.POST)
    if len(errors):
       for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
       return redirect('/blog/edit/'+id)
    else:
        blog = Blog.objects.get(id = id)
        blog.name = request.POST['name']
        blog.desc = request.POST['desc']
        blog.save()
        return redirect('/blogs')