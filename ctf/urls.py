from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='dashboard'),
    path("challenges", views.challenges, name="chal"),
    path("calendar", views.calendar, name='calendar'),
]
