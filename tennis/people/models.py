from django.db import models

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
        return "%s" % (name)
