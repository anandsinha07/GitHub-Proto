from django.conf.urls import url, include

from .views import ModuleCreateView, ModuleUpdateView, ModuleDeleteView

urlpatterns = [
    url(r'^create/$', ModuleCreateView.as_view(), name="module-create"),
    url(r'^update/(?P<pk>[0-9]+)/$', ModuleUpdateView.as_view(), name="module-update"),
    url(r'^delete/(?P<pk>[0-9]+)/$', ModuleDeleteView.as_view(), name="module-update"),
]
