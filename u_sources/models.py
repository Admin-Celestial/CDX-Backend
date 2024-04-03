
from django.db import models

class UploadFiles(models.Model):
    file_type = models.FileField(upload_to='media/', default='pdf')

