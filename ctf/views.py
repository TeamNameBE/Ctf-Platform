from django.shortcuts import render
from django.contrib.auth.models import User

from ctf.models import CTF, Challenge


def challenges(request, ctf_id):
    context = {
        "page_title": "Challenges",
        "challenges": Challenge.objects.filter(ctf__id=ctf_id),
        "users": User.objects.all()
    }
    return render(request, "challenges.html", context)


def calendar(request):
    context = {
        "page_title": "Calendar"
    }
    return render(request, "calendar.html", context)


def home(request):
    context = {
        "page_title": "Dashboard",
        "ctfs": CTF.objects.all()
    }
    return render(request, "home.html", context)
