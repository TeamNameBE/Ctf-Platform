from tooling.app import app

from tooling.database import conn


@app.task()
def exiftool(file_id):
    """
    Run exiftool on the given file
    """
    filename = conn.get(f"file:{file_id}:filename")
    with open("log.txt", "w+") as f:
        f.write(f"Running exiftool on {filename}")
