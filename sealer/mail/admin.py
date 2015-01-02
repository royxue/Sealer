from django.contrib import admin
from mail.models import ExtUser, Mail, MailAttachment, MailComment

# Register your models here.

admin.site.register(ExtUser)
admin.site.register(Mail)
admin.site.register(MailAttachment)
admin.site.register(MailComment)