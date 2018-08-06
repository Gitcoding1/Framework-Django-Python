# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Models):
    first_name = models.CharField(max_lenght=255)
    last_name = models.CharField(max_length= 255)
    email  = models.EmailField()
