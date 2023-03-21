from django.db import models
from django.contrib.auth import get_user_model

from django.utils import timezone
from colorfield.fields import ColorField

from teamname.settings import HACKMD_ROOT_URL


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]


class CTF(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    website = models.CharField(max_length=256, null=True)
    pad = models.CharField(max_length=256, null=True)
    rating = models.FloatField(default=50)

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
    def color(self):
        if self.rating >= 75:
            return 'red'
        elif self.rating >= 50:
            return 'yellow'
        elif self.rating >= 25:
            return 'green'
        else:
            return 'blue'

    @property
    def ctftime_score(self):
        # TODO: Check ctftime score value
        return 0

    @property
    def padLink(self):
        return f"{HACKMD_ROOT_URL}{self.pad}"

    def __str__(self):
        return self.name


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

    def __str__(self):
        return f"{self.name} - {self.ctf.name}"


class Category(models.Model):
    name = models.CharField(max_length=32)
    color = ColorField()

    def __str__(self):
        return self.name
