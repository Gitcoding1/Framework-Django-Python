# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from products import items
from django.shortcuts import render,redirect
# Create your views here.

def index(request):
    context={
        "items":items
    }
    return render(request,'amadon/index.html',context)

def process_order(request, item_id):
    for item in items:
        if item["id"] == int(item_id):
            amount_procesed = item['price'] * int(request.POST['quantity'])
            purchase_of = item['product']
            quantity_of = int(request.POST['quantity'])
            print quantity_of , purchase_of

    try:
        request.session['total']
    except KeyError:
        request.session['total'] = 0

    try:
        request.session['total_items']
    except KeyError:
        request.session['total_items'] = 0

    try:
        request.session['purchase']
    except KeyError:
        request.session['purchase'] = 0
    
    try:
        request.session['amount_of']
    except KeyError:
        request.session['amount_of'] = 0

    request.session['total'] += amount_procesed
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['last_trans'] = amount_procesed
    request.session['purchase'] = purchase_of
    request.session['amount_of'] = quantity_of

    return redirect('/checkout')

def checkout(request):
    return render(request, 'amadon/checkout.html')
