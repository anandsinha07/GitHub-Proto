from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import signals
from tastypie.models import create_api_key


# Create your models here.

User = get_user_model()

class Module(models.Model):
	user 			= models.ManyToManyField(User, related_name="modules")
	title			= models.CharField(max_length=150)
	version			= models.IntegerField(default=0)
	dev_id			= models.IntegerField(default=0)
	developer		= models.CharField(max_length=150, default="Codevisor Team")
	description		= models.TextField(default="Some description")
	languages		= models.TextField(default="Python")
	NumberOfInputs	= models.BigIntegerField(default=0)
	InputDescription= models.TextField(default="Some description")
	InputType		= models.CharField(max_length=150, default="Some type")
	Optional		= models.CharField(max_length=150, default="Optional")
	SubstitutedCode	= models.TextField(default="Some code")
	var_decl		= models.CharField(max_length=150, blank=True)
	Indent 			= models.BooleanField(default=False)
	IsInFunction	= models.BooleanField(default=False)
	timestamp		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

signals.post_save.connect(create_api_key, sender=User)
