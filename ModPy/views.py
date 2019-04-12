from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import CreateModuleForm, UpdateModuleForm
from .models import Module
# Create your views here.

class HomeView(TemplateView):
	template_name = "index.html"

class ConsoleView(TemplateView):
	template_name = "console.html"

class ModuleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	template_name = "developer-create.html"
	form_class = CreateModuleForm
	success_url = "/u/"

	def test_func(self):
		return self.request.user.is_superuser

class ModuleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	template_name = "developer-update.html"
	form_class = UpdateModuleForm
	success_url = "/u/"

	def get_object(self, *args, **kwargs):
		pk = self.kwargs.get("pk")
		obj = get_object_or_404(Module, id=pk) # or pk = rest_id
		return obj

	def test_func(self):
		return self.request.user.is_superuser

class ModuleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Module
	success_url = "/"

	def test_func(self):
		return self.request.user.is_superuser
