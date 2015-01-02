from django.conf.urls import patterns, url
import mail.views

urlpatterns = patterns(
	'',
	url(r'^$', mail.views.IndexView.as_view()),
	)