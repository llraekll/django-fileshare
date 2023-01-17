from django.urls import path
from .views import *

urlpatterns = [
    path('handle', HandleFileUpload.as_view(), name='handle'),
    path('', home, name='home'),
    path('download/<uid>/' ,download, name='download'),
]
