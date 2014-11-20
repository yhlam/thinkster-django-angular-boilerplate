from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from authentication.views import UserCreateView


urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/v1/users/$', UserCreateView.as_view(), name='user-create'),

    url('^.*$', TemplateView.as_view(template_name='index.html'), name='index'),
)
