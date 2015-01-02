import mail.models
import tastypie
import tastypie.authorization
from tastypie.exceptions import BadRequest
import tastypie.resources
import tastypie.serializers
import tastypie.utils
from tastypie.constants import ALL_WITH_RELATIONS


class MailResource(tastypie.resources.ModelResource):

	class Meta:
		serializers = tastypie.serializers.Serializer(formats=['json', 'xml'])
		queryset = mail.models.Mail.objects.all()
		resource_name = 'mail'
