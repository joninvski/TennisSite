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

    class Admin:
        pass

    def __str__(self):
        return "%s" % (self.name)

class ClubStudent(models.Model):
    """A student of the club """
    person = models.OneToOneField(Person)

    class Admin:
        pass

    def __str__(self):
        return "Membro: " % (self.person)

class SchoolStudent(models.Model):
    """An outside student of the school (like Desporto escular) """
    person = models.OneToOneField(Person)
    number = models.IntegerField()

    class Admin:
        pass

    def __str__(self):
        return "Aluno %s: %s" % (self.number, self.person)
