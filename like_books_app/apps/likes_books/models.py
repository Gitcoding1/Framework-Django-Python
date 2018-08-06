# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=38)
    last_name = models.CharField(max_length=38)
    email = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "User object - {} {} - {} - created: {}".format(self.first_name, self.last_name, self.email, self.created_at)


class Book(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    uploader= models.ForeignKey(User, related_name='uploaded_by')
    likes = models.ManyToManyField(User,related_name='liked_by')
    def __repr__(self):
        return "Book object - {} - {} - Uploaded_by - {} - Liked_by - {} created: {}".format(self.name, self.desc,self.uploader,self.likes, self.created_at)
   
    
