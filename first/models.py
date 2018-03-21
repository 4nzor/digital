import os

import sys
from django.contrib.auth.models import User
from django.db import models
import random


class Lecture(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=500)
    time = models.CharField(max_length=5)
    date = models.DateField()

    def __str__(self):
        return self.name


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
    lectures = models.ManyToManyField(Lecture, null=True, blank=True)
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
    lecture_themes = models.ManyToManyField(Lecture, blank=True, null=True)
    type = 'org'
