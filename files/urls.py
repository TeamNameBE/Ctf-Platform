from django.urls import path, include

import files.views as views


urlpatterns = [
    path('process/', views.start_processing, name='start_processing'),
    path('<int:pk>/', views.FileView.as_view(), name='files'),
    path('private/api/', include('files.api_urls'), namespace='private-api'),
]
