from django.db import models
from django.contrib.auth import get_user_model

from django.utils import timezone
from colorfield.fields import ColorField

import ctf.utils as utils

from teamname.settings import HACKMD_ROOT_URL


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
        return f"{HACKMD_ROOT_URL}{self.pad}"


class Challenge(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    points = models.IntegerField(default=0)
    category = models.ManyToManyField("ctf.Category")
    ctf = models.ForeignKey(CTF, on_delete=models.CASCADE, null=True)
    validated = models.BooleanField(default=False)
    pad = models.CharField(max_length=256, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Create the pad here if it does not exist
        return super().save(*args, **kwargs)

    @property
    def padLink(self):
        return f"{HACKMD_ROOT_URL}{self.pad}"


class Category(models.Model):
    name = models.CharField(max_length=32)
    color = ColorField()

    def __str__(self):
        return self.name


class ChallengeFile(models.Model):
    challenge = models.ForeignKey("ctf.Challenge", on_delete=models.CASCADE)
    file = models.FileField(upload_to=utils.chall_file_upload)

    def __str__(self):
        return self.file.name

    """TODO
        BMP
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="display:inline-block;">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
        </svg>
        PNG
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="display:inline-block;">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
        </svg>
        TXT
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="display:inline-block;">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
        </svg>
    """
