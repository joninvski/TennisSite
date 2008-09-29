# -*- coding: latin-1 -*-

from django.db import models

import datetime

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

# Create your models here.
class Person(models.Model):
    """A student of the tennis school"""
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(blank='true')
    phoneNumber = models.CharField(max_length=14, blank='true')
    height = models.IntegerField(blank='true')
    weight = models.IntegerField(blank='true')
    photo = models.ImageField(upload_to='photos/')

    class Admin:
        pass

    def __unicode__(self):
        return u"%s" % (self.name)

class ClubStudent(models.Model):
    """A student of the club """
    person = models.OneToOneField(Person)

    class Admin:
        pass

    def __unicode__(self):
        return u"Sócio: %s" % (self.person)

class SchoolStudent(models.Model):
    """An outside student of the school (like Desporto escular) """
    person = models.OneToOneField(Person)
    number = models.IntegerField()

    class Admin:
        pass

    def __unicode__(self):
        return u"Aluno %s: %s" % (self.number, self.person)
