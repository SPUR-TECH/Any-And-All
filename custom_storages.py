# Custom storage from code institute Boutique Ado -->

'''
Imports relevant django packages
'''
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """
    Directs Django to static files configuration in settings.py
    """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """
    Directs Django to media files configuration in settings.py
    """
    location = settings.MEDIAFILES_LOCATION
