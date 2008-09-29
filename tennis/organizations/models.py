from django.db import models

# Create your models here.

class Company(models.Model):
    """A student of the tennis school"""
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=14, blank='true')

    class Admin:
        pass

    def __str__(self):
        return "%s" % (self.name)


class Document(models.Model):
    """A student of the tennis school"""
    name = models.CharField(max_length=100)
    url = models.URLField(blank='false', max_length=200)
    company = models.ForeignKey(Company)

    class Admin:
        pass

    def __str__(self):
        return "%s" % (self.name)

