import os

import sys
from django.contrib.auth.models import User
from django.db import models
import random

from django_countries.fields import CountryField


def flag_upload_to(instance, filename):
    rand = random.randrange(0, sys.maxsize)
    rand = str(rand)
    return os.path.join('flag/' + instance.country, rand + os.path.splitext(filename)[1])


class Mapcheck(models.Model):
    class Meta:
        verbose_name = 'Mapcheck'
        verbose_name_plural = 'Mapchecks'

    place = models.CharField(max_length=200, blank=True, null=True)
    coord_long = models.FloatField(max_length=50, blank=True, null=True)
    coord_lat = models.FloatField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.place


class Flags(models.Model):
    country = models.CharField(max_length=200)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.country