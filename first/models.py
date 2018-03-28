import os

import sys
from django.contrib.auth.models import User
from django.db import models
import random

from First_proj import settings


def avatar_upload_to(instance, filename):
    rand = random.randrange(0, sys.maxsize)
    rand = str(rand)
    return os.path.join('avatars/' + instance.username, rand + os.path.splitext(filename)[1])


class Account(User):
    full_name = models.CharField(max_length=200)
    sex = models.CharField(max_length=200, null=True, blank=True, default='None')
    avatar = models.ImageField(upload_to=avatar_upload_to, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True, default='United States')
    placeOfWork = models.CharField(max_length=300, null=True, blank=True, default='None')
    position = models.CharField(max_length=200, null=True, blank=True, default='Professor')
    scientific_interest = models.CharField(max_length=500, null=True, blank=True, default='None')
    science_degree = models.CharField(max_length=200, null=True, blank=True, default='None')
    academic_rank = models.CharField(max_length=200, null=True, blank=True, default='None')
    researcher_id = models.CharField(max_length=200, null=True, blank=True, default='None')
    orc_id = models.URLField(max_length=300, null=True, blank=True, default='None')
    is_active = False
    type = 'user'

    def __str__(self):
        return self.username

    @classmethod
    def add_lecture(cls, user, new_lecture):
        lectures, created = cls.objects.get_or_create(
            username=user
        )
        lectures.lectures.add(new_lecture)


class Org(User):
    full_name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to=avatar_upload_to, null=True, blank=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    resperative = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    director = models.CharField(max_length=200, blank=True, null=True)
    director_email = models.EmailField(max_length=200, blank=True, null=True)
    lecture_themes = models.CharField(max_length=200, blank=True, null=True)
    type = 'org'


class Platform(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    platform_country = models.CharField(max_length=200, blank=True, null=True)
    platform_city = models.CharField(max_length=200, blank=True, null=True)
    platform_adress = models.CharField(max_length=200, blank=True, null=True)
    lat = models.FloatField()
    lng = models.FloatField()
    Org = models.ForeignKey(Org, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class App(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    country = models.CharField(max_length=200, blank=True, null=True)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    lecture_title = models.CharField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=200, blank=True, null=True)
    this_lect_is = models.CharField(max_length=200, blank=True, null=True)
    is_consired = models.BooleanField(default=False)
    check_anycity = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    is_canceled = models.BooleanField(default=False)

    def __str__(self):
        return self.lecture_title


class Language(models.Model):
    language = models.CharField(max_length=200, blank=True, null=True)


from django_countries.fields import CountryField


class Person(models.Model):
    name = models.CharField(max_length=100)
    country = CountryField()
