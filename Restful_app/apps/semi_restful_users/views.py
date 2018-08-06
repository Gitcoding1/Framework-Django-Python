# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from models import *


# Create your views here.

def index(request):
    restful_users = { 
        "users" : User.objects.all()
    }
    return render(request, 'index.html', restful_users)

def new_user(request):
    return render(request,'new_user.html')

def show(request,userid):
   return render(request,'show.html', { 'user':User.objects.get(id=userid) })

def create(request):
    if request.method == "POST":
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        print request.POST['first_name'] +' '+ request.POST['last_name'] + ' ' + request.POST['email'] 
    return redirect(reverse('users'), new_user)

def edit(request,userid):
    return render(request, "edit_user.html", { 'user': User.objects.get(id=userid) } )

def update(request,userid):
    if request.method == 'POST':
        user_updated = User.objects.filter(id=userid).update( first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect(reverse('users'),user_updated)

def delete(request,userid):
        User.objects.get(id=userid).delete()
    return redirect(reverse('users'))