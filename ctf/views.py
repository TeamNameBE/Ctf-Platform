from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello")


def challenges(request):
    return render(request, "challenges.html")


def calendar(request):
    return render(request, "calendar.html")


def listCtf(request):
    return render(request, "list.html")
