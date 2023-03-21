from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from files.models import ChallengeFile


@login_required
def start_processing(request, file_id):
    """
    Starts processing the file
    """
    file = get_object_or_404(ChallengeFile, id=file_id)
    file.process_file()
    return HttpResponse(status=204)
