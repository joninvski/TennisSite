from django.db import models

# Create your models here.

class Company(models.Model):
    """A company associated with the tennis school"""
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=14, blank='true')
    address = models.CharField(max_length=100, blank='true')

    class Admin:
        pass

    def __unicode__(self):
        return "%s" % (self.name)


class Document(models.Model):
    """A document that is associated with a company"""
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
    company = models.ForeignKey(Company)

    class Admin:
        pass

    def __unicode__(self):
        return "%s" % (self.name)

