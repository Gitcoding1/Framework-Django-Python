# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    print ('\n --- you are in the index method --\n')
    return render(request,'survey_form/index.html')

def process(request):
    print ('\n----- im the process method ---\n')
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['database'] = request.POST['database']
    request.session['comment'] = request.POST['comment']
    print request.POST
    return redirect('/results')

def results(request):
    print('\n --- you are viewing the results page ---\n')
    if request.method == "POST":
        try:
            request.session = 0
        except KeyError:
            request.session = 1
    return render(request,'survey_form/results.html')