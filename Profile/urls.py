from django.conf.urls import url, include

from .views import ProfileDetailView, ProfileUpdateView


urlpatterns = [
    url(r'^$', ProfileDetailView.as_view(), name="detail"),
    url(r'^edit/$', ProfileUpdateView.as_view(), name="edit"),
]
