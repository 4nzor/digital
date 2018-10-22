import os
import sys
from django.contrib.auth.models import User
from django.db import models
import random


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
    class Meta:
        verbose_name_plural = 'Flags'

    country = models.CharField(max_length=200)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.country


class Question(models.Model):
    question = models.CharField(max_length=200)
    status = models.BooleanField(verbose_name="active", default=True)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.question


class Organization(models.Model):
    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'

    country = models.CharField(max_length=200, blank=True, null=True)
    owner_name = models.CharField(max_length=200, blank=True, null=True)
    org_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='organization name')
    location = models.CharField(max_length=200, blank=True, null=True)
    site = models.CharField(max_length=200, blank=True, null=True)
    contact_person = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    inst_type = models.CharField(max_length=200, blank=True, null=True)
    short_description_org = models.TextField(blank=True, null=True)
    short_description_infr = models.CharField(max_length=200, blank=True, null=True)
    sci_area = models.CharField(max_length=200, blank=True, null=True)
    activities = models.CharField(max_length=200, blank=True, null=True)
    conditions_on_access = models.CharField(max_length=200, blank=True, null=True)
    restrictions = models.CharField(max_length=200, blank=True, null=True)
    inter_cooperation = models.CharField(max_length=200, blank=True, null=True)
    is_confirm = models.BooleanField(default=False, verbose_name='accepted')
    hided = models.BooleanField(default=False,verbose_name='hidden')
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)

    # def __str__(self):
    #     return self.org_name


class C0untry(User):
    orgs = models.ManyToManyField(Organization, blank=True)


class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title