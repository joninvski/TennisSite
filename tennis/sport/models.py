from django.db import models
from tennis.competition.models import *

# Create your models here.

class SingleMatch(models.Model):
    """A tennis match"""
    date = models.DateField()
    competition = models.ForeignKey(Competition)

    class Admin:
        pass

    def get_results(self):
        """
        Gets the results for a match
        """
        return SetResult.objects.filter(match=self.id).order_by('order')

    def get_results_by_competitor(self, competitor):
        """
        Gets the results of a competitor for a match
        """
        return SetResult.objects.filter(match=self.id, competitor=competitor.id).order_by('order')

    def __str__(self):
        return "Partida %s -> %s" % (self.date, self.get_results())

    def get_winner(self, competitor):
        """
        Gets the results of a competitor for a match
        """
        return SetResult.objects.filter(match=self.id, competitor=competitor.id).order_by('order')

    def get_participants(self):
        """
        Gets the participants of a match
        """
        results = self.get_results()

        participants = []
        for result in results:
            participants.append(result.competitor)

        return set(participants)

    def __str__(self):
        return "Partida %s -> %s" % (self.date, self.get_results())

class SetResult(models.Model):
        """Represents a Set game"""
        order = models.IntegerField()
        match = models.ForeignKey(SingleMatch)
        games = models.IntegerField()
        competitor = models.ForeignKey(Competitor)

        class Admin:
            pass

        def __str__(self):
            return "Set number %s: %s" % (self.order, self.games)
