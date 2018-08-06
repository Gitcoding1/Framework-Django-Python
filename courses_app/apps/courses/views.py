# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from models import * 

# Create your views here.

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request,'index.html', context)

def create(request):
    if request.method == "POST":
        d = request.POST
        print d 
        errors = Course.objects.validate(d)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
                print "TAGS: "+tag +' ' + error
        else:
            Course.objects.create(name=d['name'], description=d['description'])
            
    return redirect(reverse('courses'))

def delete(request,courseid):
    context = {
        'course': Course.objects.get(id=courseid)
    }
    return render(request,'confirm.html',context)

def destroy(request,courseid):
    Course.objects.get(id=courseid).delete()
    return redirect(reverse('courses'))