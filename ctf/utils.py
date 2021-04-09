def chall_file_upload(instance, filename):
    return "/".join(["media", instance.challenge, filename])
