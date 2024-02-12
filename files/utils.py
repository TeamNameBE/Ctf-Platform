import pickle

from tooling.utils import get_task_status, get_task_data


def chall_file_upload(instance, filename):
    return "/".join([instance.challenge.name, filename])


def get_class_from_status(status: int):
    if status == 0:
        return "light"
    elif status == 1:
        return "warning"
    elif status == 2:
        return "success"
    else:
        return "danger"


def check_statuses(file, tasks: list) -> dict:
    if file.file_type is None:
        return {"error": "The file as not yet been preprocessed"}

    result = {
        "error": None
    }
    for task_name, task in tasks.items():
        # Check if the task is applicable
        if (file.file_type in task["accepts"] or "__all__" in task["accepts"]):
            # Get status of the task
            applicable = True
            task_status = get_task_status(task_name, file.id)
            task_data = get_task_data(task_name, file.id)
            if task_data is not None:
                task_data = pickle.loads(task_data)
        else:
            applicable = False
            task_status = -1
            task_data = None

        result[task_name] = {
            "applicable": applicable,
            "status": task_status,
            "data": task_data,
            "color": get_class_from_status(task_status),
            "accepts": task["accepts"],
        }

    return result
