from django.db import models
from files.utils import chall_file_upload


class ChallengeFile(models.Model):
    challenge = models.ForeignKey("ctf.Challenge", on_delete=models.CASCADE)
    file = models.FileField(upload_to=chall_file_upload)

    processed = models.BooleanField(default=False)

    def process_file(self):
        """
        Extract file type from exiftool and run appropriate tooling on it.
        """
        pass

    def __str__(self):
        return self.file.name

    def get_icon(self):
        return "fas fa-file"
