from django.conf import settings
import os

FILE_TYPE_CHOICES = (
        ('im', 'Image'),
        ('vi', 'Video'),
        ('au', 'Audio'),
        )


STATIC_FILE_PATH = os.path.join('mail')