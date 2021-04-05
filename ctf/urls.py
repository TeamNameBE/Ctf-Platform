from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("challenges", views.challenges, name="chal"),
    path("calendar", views.calendar, name='calendar'),
    path("list_ctf", views.listCtf, name='listCtf')
]
