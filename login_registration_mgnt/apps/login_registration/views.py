# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from .forms import RegistrationForm, LoginForm

# Create your views here.
def index(request):
    forms={ 
        "registerForm" : RegistrationForm(),
        "loginForm" : LoginForm()
    }
    return render(request,'login_reg.html',forms)

def register(request):
    if request.method == "POST":
        errors = []
        form = RegistrationForm(request.POST)
        if errors:
            errors.messages.append('there is errors')
            print errors
            print request.POST["first_name"] +' '+ request.POST['last_name'] +' '+ request.POST['email'] + ' '+ request.POST['password']
    return redirect(reverse('home')) 

