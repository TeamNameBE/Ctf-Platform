from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ctf.models import CTF


@login_required
def home(request):
    context = {"page_title": "Dashboard", "ctfs": CTF.objects.all().order_by("-start_date")}
    return render(request, "home.html", context)
