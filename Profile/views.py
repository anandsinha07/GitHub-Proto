from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.conf import settings

from .forms import RegisterForm, EditProfileForm

# Create your views here.

User = get_user_model()

class RegisterView(CreateView):
	template_name = "registration/register.html"
	form_class = RegisterForm
	success_url = "/"

class ProfileDetailView(LoginRequiredMixin, DetailView):
	template_name = "profile.html"

	def get_object(self):
		return self.request.user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
	template_name = "registration/update.html"
	form_class = EditProfileForm
	success_url = "/u/"

	def get_object(self):
		return self.request.user

	def get_form_kwargs(self):
		kwargs = super(ProfileUpdateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

