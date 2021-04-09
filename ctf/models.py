from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.utils import timezone
from colorfield.fields import ColorField

import ctf.utils as utils


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]


class CTF(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    website = models.CharField(max_length=256, null=True)
    pad = models.CharField(max_length=256, null=True)

    def save(self, *args, **kwargs):
        # Create the pad here if it does not exist
        return super().save(*args, **kwargs)

    @property
    def is_finished(self):
        return timezone.now() > self.end_date

    @property
    def is_now(self):
        return self.start_date < timezone.now() < self.end_date

    @property
    def time_left(self):
        return self.end_date - timezone.now()

    @property
    def score(self):
        total = 0
        for chall in self.challenge_set.filter(validated=True):
            total += chall.points
        return total

    @property
    def ctftime_score(self):
        # TODO: Check ctftime score value
        return 0

    @property
    def padLink(self):
        return f"https://hackmd.teamna.me/{self.pad}"


class Challenge(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    points = models.IntegerField(default=0)
    category = models.ManyToManyField("ctf.Category")
    ctf = models.ForeignKey(CTF, on_delete=models.CASCADE, null=True)
    validated = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), null=True, blank=True)
    pad = models.CharField(max_length=256, null=True)

    def save(self, *args, **kwargs):
        # Create the pad here if it does not exist
        return super().save(*args, **kwargs)

    @property
    def padLink(self):
        return f"https://hackmd.teamna.me/{self.pad}"


class Category(models.Model):
    name = models.CharField(max_length=32)
    color = ColorField()

    def __str__(self):
        return self.name


class ChallengeFile(models.Model):
    challenge = models.ForeignKey("ctf.Challenge", on_delete=models.CASCADE)
    file = models.FileField(upload_to=utils.chall_file_upload)
