# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    desc = models.CharField(max_length=255, default="default")
    def __str__(self):
        return "Id: {} | Name: {} | State: {} | City: {} | Description: {}".format(self.id,self.name,self.state,self.city,self.desc)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255) 
    dojo = models.ForeignKey(Dojo, related_name='dojos')
    def __str__(self):
        return "Id: {} | First Name: {} | Last Name: {} | Dojo: {}".format(self.id,self.first_name,self.last_name,self.dojo)