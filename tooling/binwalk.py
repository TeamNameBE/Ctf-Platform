"""
Binwalk implementation as a Celery task.

API documentation:
https://github.com/ReFirmLabs/binwalk/blob/master/API.md

Minigrim0 - 2023
"""

import binwalk as bw
import logging

from app import app

logger = logging.getLogger("[Tooling] Binwalk")


@app.task
def binwalk(file_id: str, extract=False):
    """
    Runs binwalk on a file. Extracts the file if exctract is True.

    Args:
        file_id (str, optional): the ID of the file to process.
        exctract (bool, optional): Wether to extract the embedded files. Defaults to False.
    """
    logger.info("Binwalk task started")
    bw.scan(file_id, extract)
    logger.info("Binwalk task finished")
