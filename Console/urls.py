from django.conf.urls import url, include

from .views import ProgramDeleteView, ProgramCreateView, ProgramUpdateView

from ModPy.api import ModuleResource, UserResource, ProfileResource

module_resource = ModuleResource()
user_resource = UserResource()
profile_resource = ProfileResource()

urlpatterns = [
    url(r'^delete/(?P<pk>[\w-]+)/$', ProgramDeleteView.as_view(), name="program-delete"),
    url(r'^create/$', ProgramCreateView.as_view(), name="program-create"),
    url(r'^c/(?P<pk>[0-9]+)/$', ProgramUpdateView.as_view(), name="program-update"),
    url(r'^api-mod/', include(module_resource.urls)),
    url(r'^api-user/', include(user_resource.urls)),
    url(r'^api-profile/', include(profile_resource.urls)),
]
