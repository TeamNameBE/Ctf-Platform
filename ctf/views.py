from django.http import HttpResponseRedirect, HttpResponseNotAllowed, HttpResponseBadRequest
from django.contrib import messages
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from ctf.models import CTF, Challenge, ChallengeFile
from ctf.forms import ChallengeForm


@login_required
def challenges(request, ctf_id):
    if request.method == "POST":
        form = ChallengeForm(request.POST)
        if form.is_valid:
            challenge = form.save()
            challenge.ctf = get_object_or_404(CTF, id=ctf_id)
            challenge.save()

    context = {
        "page_title": "Challenges",
        "challenges": Challenge.objects.filter(ctf__id=ctf_id),
        "users": User.objects.all(),
        "ctf": get_object_or_404(CTF, id=ctf_id),
    }
    if not context["ctf"].is_finished:
        context["AddChallenge"] = ChallengeForm()
    return render(request, "challenges.html", context)


@login_required
def calendar(request):
    context = {"page_title": "Calendar"}
    return render(request, "calendar.html", context)


@login_required
def home(request):
    context = {"page_title": "Dashboard", "ctfs": CTF.objects.all().order_by("-start_date")}
    return render(request, "home.html", context)


@login_required
def validate_chall(request, ctf_id, chall_id):
    challenge = get_object_or_404(Challenge, id=chall_id)
    challenge.validated = True
    challenge.save()
    return HttpResponseRedirect(reverse("chal", kwargs={"ctf_id": ctf_id}))


@login_required
def assign_user(request, ctf_id, chall_id):
    # TODO
    return HttpResponseRedirect(reverse("chal", kwargs={"ctf_id": ctf_id}))


@login_required
def upload_file(request, ctf_id, chall_id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["GET"])

    file = request.FILES.get("file", None)
    print(request.FILES)
    print(file)
    if file is None:
        messages.error(request, "Fichier manquant")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])

    response = ChallengeFile.objects.create(file=file, challenge=get_object_or_404(Challenge, id=chall_id))

    print(response)
    return HttpResponseRedirect(reverse("chal", kwargs={"ctf_id": ctf_id}))
