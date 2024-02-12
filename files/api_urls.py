from django.urls import path

import files.api_views as views


urlpatterns = [
    path("<int:pk>/update/type", views.update_file_type, name='files'),
]
