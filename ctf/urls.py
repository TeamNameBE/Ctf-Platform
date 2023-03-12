from django.urls import path
from . import views

urlpatterns = [
    path("<int:ctf_id>/challenges", views.challenges, name="chal"),
    path("<int:ctf_id>/challenges/<int:chall_id>/validate", views.validate_chall, name="validate_chall"),
    path("<int:ctf_id>/challenges/<int:chall_id>/upload", views.upload_file, name="upload_file"),
    path("<int:ctf_id>/challenges/edit/<int:chall_id>/", views.edit_chall, name="editchall"),
]
