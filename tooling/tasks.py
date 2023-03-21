"""
Celery Tasks.

Minigrim0 - 2023
"""

import binwalk as bw
import exiftool as exif
import logging

from tooling.app import app
from tooling.database import conn

logger = logging.getLogger("[Tooling] Binwalk")


@app.task
def binwalk(file_id: str, extract=False):
    """
    Runs binwalk on a file. Extracts the file if exctract is True.

    API documentation:
    https://github.com/ReFirmLabs/binwalk/blob/master/API.md

    Args:
        file_id (str, optional): the ID of the file to process.
        extract (bool, optional): Wether to extract the embedded files.
        Defaults to False.
    """
    logger.info("Binwalk task started")
    bw.scan(file_id, extract)
    logger.info("Binwalk task finished")


@app.task()
def exiftool(file_id):
    """
    Run exiftool on the given file
    """
    logger.info(f"[file-{file_id}] Starting exiftool")
    filename = conn.get(f"file:{file_id}:filename").decode("utf-8")
    filename = "/media" / filename
    logger.info(f"[file-{file_id}] Filename: {filename}")
    with exif.ExifTool() as et:
        metadata = et.get_metadata(filename)
        logger.info(f"[file-{file_id}] Saving metadata")
        conn.set(f"file:{file_id}:metadata", metadata)
