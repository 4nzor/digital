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

    country = models.CharField(max_length=200, blank=True, null=True, verbose_name='Name of the Country')
    owner_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Name and Contact Details')
    org_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Name of organization/ owner')
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name='Location of the center (city)')
    site = models.CharField(max_length=200, blank=True, null=True, verbose_name='Web-site')
    contact_person = models.CharField(max_length=200, blank=True, null=True, verbose_name='Contact person')
    email = models.CharField(max_length=200, blank=True, null=True, verbose_name='Email Tel Fax')
    inst_type = models.CharField(max_length=200, blank=True, null=True, verbose_name='Institution type')
    short_description_org = models.TextField(blank=True, null=True, verbose_name='Short description of organization')
    short_description_infr = models.CharField(max_length=200, blank=True, null=True, verbose_name='Short description of research infrastructure')
    sci_area = models.CharField(max_length=200, blank=True, null=True, verbose_name='Scientific area (thematic areas to be defined)')
    activities = models.CharField(max_length=200, blank=True, null=True, verbose_name='Activities undertaken and services provided for users')
    conditions_on_access = models.CharField(max_length=200, blank=True, null=True, verbose_name='Conditions for access to the equipment or facilities for research infrastructure staff')
    restrictions = models.CharField(max_length=200, blank=True, null=True, verbose_name='Restrictions on access to the equipment or facility')
    inter_cooperation = models.CharField(max_length=200, blank=True, null=True, verbose_name='International cooperation activities')
    is_confirm = models.BooleanField(default=False, verbose_name='accepted')
    hided = models.BooleanField(default=False, verbose_name='hidden')
    lat = models.FloatField(default=0)
    lon = models.FloatField(default=0)

    def get_fields_and_values(self):
        return [(field, field.value_to_string(self)) for field in Organization._meta.fields]


class C0untry(User):
    orgs = models.ManyToManyField(Organization, blank=True)


class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
