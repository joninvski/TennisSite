from django.db import models

import datetime

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

# Create your models here.
class Person(models.Model):
    """A student of the tennis school"""
    name = models.CharField(maxlength=100)
    birthday = models.DateField()
    gender = models.CharField(maxlength=1, choices=GENDER_CHOICES)
    email = models.EmailField(blank='true')
    phoneNumber = models.CharField(maxlength=14, blank='true')

    class Admin:
        pass

    def __str__(self):
        return "%s" % (self.name)

    @property
    def age(self):
        """
        Calculates the age of an athlete
        """
        TODAY = datetime.date.today()
        return u"%s" % dateutil.relativedelta(TODAY, self.birthday).years

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
    
    class Admin:
        pass

    def __str__(self):
        return "Aluno: %s" % (self.person) 
