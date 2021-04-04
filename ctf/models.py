from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

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


class Ctf(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    website = models.TextField()
    pad = models.TextField()


class Challenges(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    points = models.IntegerField(default=0)
    category = models.TextField(choices=CATEGORY)
    ctf = models.ForeignKey(Ctf, on_delete=models.CASCADE)
    validate = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    pad = models.TextField()
