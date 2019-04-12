from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from CodeVisor.utils import unique_slug_generator

# Create your models here.

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
	user 			= models.OneToOneField(User, on_delete=models.CASCADE)
	description 	= models.TextField(blank=True, null=True, default="Not provided")
	education		= models.CharField(max_length=120, blank=True, null=True, default="Not provided")
	company 		= models.CharField(max_length=120, blank=True, null=True, default="Not provided")
	activation_key 	= models.CharField(max_length=120, blank=True, null=True)
	activated 		= models.BooleanField(default=False)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username

	def get_programs(self):
		return self.user.programs.all()

def post_save_receiver(sender, instance, created, *args, **kwargs):
	profile, is_created = Profile.objects.get_or_create(user=instance)


post_save.connect(post_save_receiver, sender=User)
