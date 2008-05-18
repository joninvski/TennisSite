from django.db import models
from tennis.people.models import *

# Create your models here.
class Tournament(models.Model):
    """A ladder Tournament"""
    competitors = models.ManyToManyField(Competitor)
    startDate = models.DateField()
    endDate = models.DateField()
    name = models.CharField(maxlength=50)

    class Admin:
        pass

    def __str__(self):
        return "%s de %s a %s" % (self.name, self.startDate, self.endDate)

    def sortRanking(self):
        """
        Sort the ranking
        """
        pass
