from django.urls import path

import files.views as views


urlpatterns = [
    path('process/', views.start_processing, name='start_processing'),
]
