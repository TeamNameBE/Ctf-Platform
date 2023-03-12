from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ctf.models import CTF
from ctf.forms import CTForm


@login_required
def home(request):
    context = {
        "page_title": "Dashboard",
        "ctfs": CTF.objects.all().order_by("-start_date")
    }
    return render(request, "home.html", context)


@login_required
def calendar(request):
    context = {
        "page_title": "Calendar",
        "events": CTF.objects.all(),
        "form": CTForm(),
    }
    return render(request, "calendar.html", context)
