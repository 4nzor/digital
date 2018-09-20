import os

import sys
from django.contrib.auth.models import User
from django.db import models
import random


def avatar_upload_to(instance, filename):
    rand = random.randrange(0, sys.maxsize)
    rand = str(rand)
    return os.path.join('avatars/' + instance.username, rand + os.path.splitext(filename)[1])


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

