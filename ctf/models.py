from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.utils import timezone


CATEGORY = {
    ("forensic", "forensic"),
    ("stegano", "stegano"),
    ("pwn", "pwn"),
    ("crypto", "crypto"),
    ("reverse", "reverse"),
    ("osint", "osint"),
}


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
        return 0


class Challenges(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    points = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORY)
    ctf = models.ForeignKey(CTF, on_delete=models.CASCADE)
    validated = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    pad = models.CharField(max_length=256, null=True)

    def save(self, *args, **kwargs):
        # Create the pad here if it does not exist
        return super().save(*args, **kwargs)
