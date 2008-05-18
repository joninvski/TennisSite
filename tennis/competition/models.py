from django.db import models
from tennis.people.models import *

# Create your models here.
class Competition(models.Model):
    """A ladder competition"""
    startDate = models.DateField()
    endDate = models.DateField()
    name = models.CharField(maxlength=50)

    def __str__(self):
        return "%s de %s a %s" % (self.name, self.startDate, self.endDate)

    def sortRanking(self):
        """
        Sort the ranking
        """
        pass

    def get_competitors(self):
        """
        Get the list of the competitors of this competition
        """
        return Competitor.objects.filter(competition=self.id)

    class Admin:
        pass

class Competitor(models.Model):
    """Defines a competitor in a tennis competition"""
    gamesPlayed = models.IntegerField()
    gamesWon = models.IntegerField()
    gamesTied = models.IntegerField()
    gamesLost = models.IntegerField()
    person = models.ForeignKey(Student)
    competition = models.ForeignKey(Competition)
    rank = models.IntegerField()

    class Admin:
        pass

    def __str__(self):
        return "%d. %s -> Jogados: %d Victorias: %d Empates: %d Derrotas: %d" % ( self.rank, self.person, self.gamesPlayed, self.gamesWon, self.gamesTied, self.gamesLost)
