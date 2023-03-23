"""
Celery Tasks.

Minigrim0 - 2023
"""
import pickle
import binwalk as bw
import exiftool as exif
import logging

from tooling.app import app
from tooling.utils import (
    set_task_status,
    get_task_status,
    set_task_data,
    get_task_data,
    get_filename
)
import tooling.status as status
from files.models import ChallengeFile


logger = logging.getLogger("[Tooling/tasks]")


@app.task()
def exiftool(file_id: int):
    """
    Run exiftool on the given file
    """
    TASK = "exiftool"

    set_task_status(TASK, file_id, status.RUNNING)
    logger.info(f"[exiftool-{file_id}] Starting exiftool")
    filename = get_filename(file_id)
    logger.info(f"[exiftool-{file_id}] Filename: {filename}")
    try:
        with exif.ExifToolHelper() as et:
            metadata = et.get_metadata(filename)[0]
            logger.info(f"[exiftool-{file_id}] Saving metadata")
            set_task_data(TASK, file_id, pickle.dumps(metadata))
            set_task_status(TASK, file_id, status.SUCCESS)
    except Exception as e:
        logger.error(f"[exiftool-{file_id}] Error: {e}")
        set_task_data(TASK, file_id, pickle.dumps(e))
        set_task_status(TASK, file_id, status.ERROR)
    logger.info(f"[exiftool-{file_id}] Exiftool finished")

    logger.info(f"[exiftool-{file_id}] Updating file metadata")
    file = ChallengeFile.objects.get(id=file_id)
    file.processed = True
    file.file_type = metadata["File:MIMEType"]
    file.save()
    logger.info(f"[exiftool-{file_id}] File metadata updated")

    next_tasks.delay(file_id)


@app.task
def binwalk(file_id: int, extract=False):
    """
    Runs binwalk on a file. Extracts the file if exctract is True.

    API documentation:
    https://github.com/ReFirmLabs/binwalk/blob/master/API.md

    Args:
        file_id (str, optional): the ID of the file to process.
        extract (bool, optional): Wether to extract the embedded files.
        Defaults to False.
    """
    TASK = "binwalk"

    set_task_status(TASK, file_id, status.RUNNING)
    filename = get_filename(file_id)
    results = bw.scan(filename)
    set_task_data(TASK, file_id, pickle.dumps(results))
    set_task_status(TASK, file_id, status.SUCCESS)


@app.task
def unzip(file_id: int):
    pass


@app.task
def strings(file_id: int):
    pass


# Task definitions
tasks = {
    "exiftool": {
        "task": exiftool,
        "accepts": ["__all__"],
    },
    "binwalk": {
        "task": binwalk,
        "accepts": ["__all__"],
    },
    "zip_observe": {
        "task": unzip,
        "accepts": ["zip"],
    },
    "strings": {
        "task": strings,
        "accepts": ["__all__"],
    }
}


@app.task()
def next_tasks(file_id: int):
    """
    Finds the next tasks to run for the given file

    Args:
        file_id (_type_): _description_
    """
    # Check if the file has been pre-processed (exiftool)
    if get_task_status("exiftool", file_id) == str(status.SUCCESS):
        # Check if the file is a JPEG
        metadata = pickle.loads(get_task_data("exiftool", file_id))
        mime_type = metadata["File:MIMEType"].split("/")[1]
        tasks_started = []
        logger.info(f"[dispatch-{file_id}] Mime type: {mime_type}")
        for task in tasks:
            if task == "exiftool":
                continue
            if mime_type in tasks[task]["accepts"] or "__all__" in tasks[task]["accepts"]:
                tasks[task]["task"].delay(file_id)
                tasks_started.append(task)

        if len(tasks_started) == 0:
            logger.info(f"[dispatch-{file_id}] No tasks started")
            set_task_status("dispatch", file_id, status.SUCCESS)
        else:
            logger.info(
                f"[dispatch-{file_id}] Tasks started: {', '.join(tasks_started)}"
            )
            set_task_status("dispatch", file_id, status.SUCCESS)
    else:
        logger.error(
            f"[dispatch-{file_id}] File not pre-processed or error occured")
        set_task_status("dispatch", file_id, status.FAILURE)
