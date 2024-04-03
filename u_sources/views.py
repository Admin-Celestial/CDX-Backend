from rest_framework.parsers import FileUploadParser
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import mimetypes
import uuid
import tempfile
from django.core.files.uploadedfile import InMemoryUploadedFile
#from .serializers import UploadFilesSerializer
from .models import UploadFiles
import boto3
import logging
from django.views.decorators.csrf import csrf_exempt
#from usermaster_auth.authentication import ExpiringTokenAuthentication
#from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from utils.custom_storage import CustomS3Boto3Storage
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
import os
import magic


class FileUploadView(APIView):

    parser_class = (FileUploadParser,)
    storage_class = CustomS3Boto3Storage()  

    permission_classes = [IsAuthenticated]
    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({'error': 'No file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        uploaded_file = request.FILES['file']

        try:
            
            uploaded_file_name = self.storage_class.save(uploaded_file.name, uploaded_file)
            return Response({'message': 'File uploaded successfully.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



'''


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({'error': 'No file provided.'}, status=status.HTTP_400_BAD_REQUEST)

        uploaded_file = request.FILES['file']

        # Get the content type of the uploaded file
        content_type = uploaded_file.content_type

        # Initialize AWS S3 client
        s3 = boto3.client('s3', 
                          aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                          region_name=settings.AWS_S3_REGION_NAME)
        try:
            # Upload the file directly to S3 bucket with the detected Content-Type
            s3.upload_fileobj(uploaded_file, settings.AWS_STORAGE_BUCKET_NAME, uploaded_file.name, ExtraArgs={'ContentType': content_type})
            return Response({'message': 'File uploaded successfully.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

'''



class ListAllS3Files(APIView):
    permission_classes = [IsAuthenticated]
    @method_decorator(csrf_exempt)
    def get(self, request):
        # Initialize AWS S3 client with credentials from Django settings
        s3 = boto3.client('s3', 
                          aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                          aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                          region_name=settings.AWS_S3_REGION_NAME)

        bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        folder_prefix = 'media/'

        files = []
        file_id = 1

        try:
            response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_prefix)
            objects = response.get('Contents', [])

            for obj in objects:
                key = obj['Key']
                file_name = os.path.basename(key)
                content_type, _ = mimetypes.guess_type(key)
                file_format = content_type.split('/')[-1] if content_type else ""

                files.append({'id': file_id, 'key': file_name, 'content_type': file_format})
                file_id += 1

            return Response(files)
        except Exception as e:
            return Response({'error': str(e)}, status=500)





















