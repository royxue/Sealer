import mail.models
import tastypie
import tastypie.authorization
from tastypie.exceptions import BadRequest
import tastypie.resources
import tastypie.serializers
import tastypie.utils
from tastypie.constants import ALL, ALL_WITH_RELATIONS


class ExtUserResource(tastypie.resources.ModelResource):

	def obj_create():
		pass

	class Meta:
		serializers = tastypie.serializers.Serializer(formats=['json', 'xml'])
		queryset = mail.models.ExtUser.objects.all()
		resource_name = 'extuser'
		always_return_data = True


class MailResource(tastypie.resources.ModelResource):
	created_by  = tastypie.fields.ForeignKey('mail.api.ExtUserResource', 'created_by')

	def dehydrate(self):
		pass

	class Meta:
		serializers = tastypie.serializers.Serializer(formats=['json', 'xml'])
		queryset = mail.models.Mail.objects.all()
		resource_name = 'mail'
		filtering = {
			'id': ALL,
			'created_by': ALL_WITH_RELATIONS,
		}
		always_return_data = True


class MailAttachmentResource(tastypie.resources.ModelResource):
	mail = tastypie.fields.ForeignKey('mail.api.MailResource', 'mail')

	class Meta:
		serializers = tastypie.serializers.Serializer(formats=['json', 'xml'])
		queryset = mail.models.MailAttachment.objects.all()
		resource_name = 'mailattachment'
		filtering = {
			'mail': ALL_WITH_RELATIONS,
		}


class MailCommentResource(tastypie.resources.ModelResource):
	mail = tastypie.fields.ForeignKey('mail.api.MailResource', 'mail')

	class Meta:
		serializers = tastypie.serializers.Serializer(formats=['json', 'xml'])
		queryset = mail.models.MailComment.objects.all()
		resource_name = 'mailcomment'
		filtering = {
			'mail': ALL_WITH_RELATIONS,
		}



