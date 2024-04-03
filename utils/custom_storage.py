from storages.backends.s3boto3 import S3Boto3Storage

class CustomS3Boto3Storage(S3Boto3Storage):
    def get_available_name(self, name, max_length=None):
        # Ensure that files are uploaded to the specified directory
        name = super().get_available_name(name, max_length)
        if name.startswith('media/'):
            return name
        return f'media/{name}'
