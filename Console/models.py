from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from CodeVisor.utils import unique_slug_generator

# Create your models here.

User = settings.AUTH_USER_MODEL

class Program(models.Model):
	owner			= models.ForeignKey(User, related_name='programs', on_delete=models.CASCADE)
	title			= models.CharField(max_length=150)
	description		= models.TextField(blank=True, null=True, default="This is some program")
	variables		= models.CharField(max_length=150, blank=True, null=True)
	code			= models.TextField(blank=True, null=True)
	slug			= models.SlugField(blank=True, null=True)
	timestamp		= models.DateTimeField(auto_now_add=True)
	updated			= models.DateTimeField(auto_now=True)
	public			= models.BooleanField(default=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-updated', '-timestamp']


def pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender=Program)
