from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

# Create your views here.

from .models import Program
from .forms import CreateProgramForm
from tastypie.models import ApiKey

from ModPy.models import Module

class ProgramDeleteView(DeleteView):
	model = Program
	success_url = reverse_lazy("profile:detail")

class ProgramCreateView(LoginRequiredMixin, CreateView):
	form_class = CreateProgramForm
	template_name = "create-program.html"
	success_url = "/u/"

	def get_form_kwargs(self):
		kwargs = super(ProgramCreateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

class ProgramUpdateView(LoginRequiredMixin, TemplateView):
	template_name = "console.html"

	def get_context_data(self, *args, **kwargs):
		prog_id = self.kwargs.get("pk")
		obj = get_object_or_404(Program, pk=prog_id)
		modules = Module.objects.filter(user=self.request.user,languages__icontains="python")
		context = {
			"modules":modules,
			"obj":obj,
			"key":ApiKey.objects.get(user=self.request.user)
		}
		return context
