from django.conf.urls import patterns, url
import mail.views

urlpatterns = patterns(
	'',
	url(r'^$', mail.views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', mail.views.MailDetailView.as_view(), name='mail_detail'),
)