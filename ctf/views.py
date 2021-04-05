from django.shortcuts import render


def challenges(request):
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
        "page_title": "Dashboard"
    }
    return render(request, "home.html", context)
