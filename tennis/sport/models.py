from django.db import models
from tennis.competition.models import Competition, Competitor

# Create your models here.

class SingleMatch(models.Model):
    """A tennis match"""
    date = models.DateField()
    competition = models.ForeignKey(Competition)
    competitorA = models.ForeignKey(Competitor, related_name="competitorA")
    competitorB = models.ForeignKey(Competitor, related_name="competitorB")

    class Admin:
        pass

    def get_results(self):
        """
        Gets the results for a match
        """
        return SetResult.objects.filter(match=self.id)

    def get_results_by_competitor(self, competitor):
        """
        Gets the results of a competitor for a match
        """
        return SetResult.objects.filter(match=self.id, competitor=competitor.id)

    def __str__(self):
        a = self.get_results()

        b = ""
        for result in a:
            b + result.__str__()

        return b # "Partida %s -> %s" % (self.date, self.get_results())

    def get_winner(self, competitor):
        """
        Gets the results of a competitor for a match
        """
        return SetResult.objects.filter(match=self.id, competitor=competitor.id)

class SetResult(models.Model):
    """Represents a Set game"""
    order = models.IntegerField()
    match = models.ForeignKey(SingleMatch)
    games = models.IntegerField()
    competitor = models.ForeignKey(Competitor)

    class Admin:
        pass

    class Meta:
        ordering = ['competitor', 'order']

    def __str__(self):
        return "%s Set number %s: %s" % (self.competitor.person.name, self.order, self.games)
