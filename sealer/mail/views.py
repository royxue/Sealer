from django.shortcuts import render
from django.views.generic import View, DetailView, TemplateView
import mail.models


class IndexView(TemplateView):

    template_name = 'mail/index.html'


class MailDetailView(DetailView):

    template_base_name = 'mail/mail_detail.html'
    model = mail.models.Mail

    def get_context_data(self, **kwargs):
        context = super(MailDetailView, self).get_context_data(**kwargs)
        return context