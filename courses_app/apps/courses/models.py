# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self,postData):
        errors = {}
        if len(postData['name']) < 6:
            errors['name'] = "Course name must be greater than 5 characters."
        if len(postData['description']) < 16:
            errors['description'] = "Course description must be greater than 15 characters."
        return errors

class Course (models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()
    def __unicode__(self):
        return "id: " + str(self.id) + ", name: " + self.name + " " + ', desc: ' + self.description