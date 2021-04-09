from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from ctf.models import CTF, Challenge


def challenges(request, ctf_id):
    context = {
        "page_title": "Challenges",
        "challenges": Challenge.objects.filter(ctf__id=ctf_id),
        "users": User.objects.all(),
        "ctf": get_object_or_404(CTF, id=ctf_id),
    }
    return render(request, "challenges.html", context)


def calendar(request):
    context = {"page_title": "Calendar"}
    return render(request, "calendar.html", context)


def home(request):
    context = {"page_title": "Dashboard", "ctfs": CTF.objects.all()}
    return render(request, "home.html", context)


def validate_chall(request, ctf_id, chall_id):
    challenge = get_object_or_404(Challenge, id=chall_id)
    challenge.validated = True
    challenge.save()
    return HttpResponseRedirect(reverse("chal", kwargs={"ctf_id": ctf_id}))


def assign_user(self, ctf_id, chall_id):
    # TODO
    return HttpResponseRedirect(reverse("chal", kwargs={"ctf_id": ctf_id}))
