from django.urls import path

import files.views as views


urlpatterns = [
    path('files/<int:file_id>/process/', views.start_processing, name='start_processing'),
]
