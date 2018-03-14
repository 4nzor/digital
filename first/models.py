import os
from django.contrib.auth.models import User
from django.db import models


class Lecture(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=500)
    time = models.CharField(max_length=5)
    date = models.DateField()

    def __str__(self):
        return self.name


def avatar_upload_to(instance, filename):
    return os.path.join('uploads', instance.user.username + os.path.splitext(filename)[1])


class Account(User):
    full_name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to=avatar_upload_to, null=True, blank=True)
    lectures = models.ManyToManyField(Lecture, null=True, blank=True)
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