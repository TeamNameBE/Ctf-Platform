def chall_file_upload(instance, filename):
    return "/".join([instance.challenge.name, filename])
