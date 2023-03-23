import redis

from django.db import models
from django.conf import settings
from files.utils import chall_file_upload


class ChallengeFile(models.Model):
    FILE_TYPES = (
        ("txt", "Text"),
        ("zip", "Zip"),
        ("pdf", "PDF"),
        ("doc", "Word"),
        ("xls", "Excel"),
        ("jpg", "JPEG"),
        ("png", "PNG"),
        ("gif", "GIF"),
        ("mp3", "MP3"),
        ("mp4", "MP4"),
        ("avi", "AVI"),
        ("mov", "MOV"),
        ("exe", "EXE"),
        ("bin", "Binary"),
    )

    challenge = models.ForeignKey("ctf.Challenge", on_delete=models.CASCADE)
    file = models.FileField(upload_to=chall_file_upload)

    processed = models.BooleanField(default=False)
    file_type = models.CharField(max_length=3, choices=FILE_TYPES, blank=True)

    parent_file = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True)

    def process_file(self):
        """
        Extract file type from exiftool and run appropriate tooling on it.
        """
        conn = redis.Redis(host=settings.REDIS_HOST, port=6379, db=0)
        conn.set(f"file:{self.id}:status", "queued")
        conn.set(f"file:{self.id}:filename", self.file.name)
        from tooling.tasks import exiftool

        exiftool.delay(self.id)

    def __str__(self):
        return self.file.name

    def get_icon(self):
        return "fas fa-file"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
