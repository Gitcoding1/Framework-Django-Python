# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=38)
    last_name = models.CharField(max_length=38)
    email = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return "id: " + str(self.id) + ", first name: " + self.first_name + ", last name: " +self.last_name + ", Email: " + self.email 