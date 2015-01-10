from django.conf.urls import patterns, include, url

from django.contrib import admin

from tastypie.api import Api
from mail.api import *

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sealer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mail/', include('mail.urls')),
)


# api
v1_api = Api(api_name = 'sealer')
v1_api.register(MailResource())
v1_api.register(ExtUserResource())
v1_api.register(MailAttachmentResource())
v1_api.register(MailCommentResource())
urlpatterns += patterns('',
    url(r'', include(v1_api.urls)),
)