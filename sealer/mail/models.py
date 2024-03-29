from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from utils.const import FILE_TYPE_CHOICES, STATIC_FILE_PATH


class ExtUser(models.Model):
    user = models.OneToOneField(User)
    wx_openid = models.CharField(max_length=256)
    wx_avatar = models.URLField(max_length=256)

    def __unicode__(self):
        return unicode(self.id)


class Mail(models.Model):
    create_by = models.ForeignKey(ExtUser, related_name='creater')
    title = models.CharField(max_length=256)
    content = models.TextField()
    create_at = models.DateTimeField(default=now)
    open_at = models.DateTimeField()
    receive_by = models.ManyToManyField(ExtUser, related_name='receiver',
                                        null=True, blank=True)

    def __unicode__(self):
        return unicode(self.id)


class MailAttachment(models.Model):

    mail = models.ForeignKey(Mail)
    f_type = models.CharField(max_length=2, choices=FILE_TYPE_CHOICES)
    attachment = models.FileField(upload_to=STATIC_FILE_PATH)

    @property
    def link(self):
        return ''.join((STATIC_FILE_PATH, self.attachment.url))


class MailComment(models.Model):
    mail = models.ForeignKey(Mail, related_name="mail_comment")
    create_by = models.ForeignKey(ExtUser)
    create_at = models.DateTimeField(default=now)
    content = models.TextField()