from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class ExtUser(models.Model):
    user = models.OneToOneField(User)
    wx_openid = models.CharField()
    wx_avatar = model.CharField()

class Mail(models.Model):
    created_by = models.ForeignKey(ExtUser)
    title = models.CharField()
    content = models.TextField()
    create_at = models.DateTimeField(default=now)
    open_at = models.DateTimeField()
    received_by = models.ManyToManyField(ExtUser)

class File(models.Model):
    FILE_TYPE_CHOICES = (
            ('im', 'Image'),
            ('vi', 'Video'),
            ('au', 'Audio'),
            )
    f_type = models.CharField(max_length=2, choices=FILE_TYPE_CHOICES)
    mail = models.ForeignKey(Mail)


class MailComment(models.Model):
    mail = models.ForeignKey(Mail)
    created_by = models.ForeignKey(ExtUser)
    create_at = model.DateTimeField(default=now)
    content = model.TextField()
    
    
