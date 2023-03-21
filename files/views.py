import logging

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from files.models import ChallengeFile

logger = logging.getLogger(__name__)


@login_required
def start_processing(request):
    """
    Starts processing the file
    """
    logger.info("Starting file processing")
    if request.method != "GET":
        return HttpResponseBadRequest("Invalid request method")

    file_id = request.GET.get("file_id", None)
    if file_id is None:
        return HttpResponseBadRequest("Missing file_id parameter")

    file = get_object_or_404(ChallengeFile, id=file_id)
    file.process_file()
    return HttpResponse(status=204)
