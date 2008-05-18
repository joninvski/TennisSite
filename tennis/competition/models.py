from django.db import models

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

    class Admin:
        pass
