
from django.urls import path
from .views import FileUploadView, ListAllS3Files

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('uploaded_files/', ListAllS3Files.as_view(), name='render-S3'),
]
