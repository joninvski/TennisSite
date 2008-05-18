from django.db import models
from tennis.competition.models import *

import datetime

# Create your models here.
class Student(models.Model):
    """A student of the tennis school"""
    name = models.CharField(maxlength=100)
    birthday = models.DateField()
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

class Competitor(models.Model):
    """Defines a competitor in a tennis competition"""
    gamesPlayed = models.IntegerField()
    gamesWon = models.IntegerField()
    gamesTied = models.IntegerField()
    gamesLost = models.IntegerField()
    person = models.ForeignKey(Student)
    competition = models.ForeignKey(Competition)

    class Admin:
        pass

    def __str__(self):
        return "%s -> Jogados: %d Victorias: %d Empates: %d Derrotas: %d" % ( self.person, self.gamesPlayed, self.gamesWon, self.gamesTied, self.gamesLost)

    def get_competition_competitor(comp):
        """
        Gets the competitors given a competition
        """
        Competitor.objects.filter(competition=comp)
