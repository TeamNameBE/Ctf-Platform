"""
Utility functions for the tooling package.

Minigrim0 - 2023
"""

import os
import logging
from tooling.database import conn
from tooling.status import STATUS_STR

logger = logging.getLogger("[Tooling/utils]")


def status_display(status: int) -> str:
    return STATUS_STR.get(status, "unknown")


def get_filename(file_id: int):
    """
    Gets the filename of a file

    Args:
        file_id (int): The ID of the file to get the filename of

    Returns:
        str: The filename of the file prefixed with the media directory
    """
    filename = conn.get(f"file:{file_id}:filename").decode("utf-8")
    return os.path.join("media", filename)


def set_task_status(task: str, file_id: int, status: int):
    """
    Sets the status of a task for a given file

    Args:
        task (str): The task to set the status for
        file_id (int): The ID of the file to set the status for
        status (int): The status to set
    """
    conn.set(f"tasks:{task}:{file_id}:status", status)
    logger.info(
        f"[{task}-{file_id}] {status_display(status)}"
    )


def get_task_status(task: str, file_id: int):
    """
    Gets the status of a task for a given file

    Args:
        task (str): The task to get the status for
        file_id (int): The ID of the file to get the status for

    Returns:
        int: The status of the task
    """
    status = conn.get(f"tasks:{task}:{file_id}:status")
    return status.decode() if status else None


def set_task_data(task: str, file_id: int, data: str):
    """
    Sets the data of a task for a given file

    Args:
        task (str): The task to set the data for
        file_id (int): The ID of the file to set the data for
        data (str): The data to set
    """
    logger.info(f"[{task}-{file_id}] saving data")
    conn.set(f"tasks:{task}:{file_id}:data", data)


def get_task_data(task: str, file_id: int):
    """
    Gets the data of a task for a given file

    Args:
        task (str): The task to get the data for
        file_id (int): The ID of the file to get the data for

    Returns:
        str: The data of the task
    """
    # No need to decode, this is pickled data
    return conn.get(f"tasks:{task}:{file_id}:data")
