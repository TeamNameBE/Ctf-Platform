from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="dashboard"),
    path("<int:ctf_id>/challenges", views.challenges, name="chal"),
    path("<int:ctf_id>/challenges/<int:chall_id>/", views.assign_user, name="assignUser"),
    path("<int:ctf_id>/challenges/<int:chall_id>/validate", views.validate_chall, name="validate_chall"),
    path("calendar", views.calendar, name="calendar"),
]
