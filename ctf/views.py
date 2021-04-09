from django.shortcuts import render

from ctf.models import CTF


def challenges(request, ctf_id):
    context = {
        "page_title": "Challenges"
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
