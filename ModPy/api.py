from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization

from django.contrib.auth import get_user_model

from .models import Module
from Profile.models import Profile

User = get_user_model()

class ModuleResource(ModelResource):

	class Meta:
		queryset = Module.objects.all()
		resource_name = "module"
		authentication = ApiKeyAuthentication()
		authorization = DjangoAuthorization()

class UserResource(ModelResource):

	class Meta:
		queryset = User.objects.all()
		resource_name = "user"
		authentication = ApiKeyAuthentication()
		authorization = DjangoAuthorization()

class ProfileResource(ModelResource):

	class Meta:
		queryset = Profile.objects.all()
		resource_name = "profile"
		authentication = ApiKeyAuthentication()
		authorization = DjangoAuthorization()