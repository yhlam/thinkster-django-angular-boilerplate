from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from authentication.views import CurrentUserView, UserCreateView


urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),

    url(r'^api/v1/users/$', UserCreateView.as_view(), name='user-create'),
    url(r'^api/v1/me/$', CurrentUserView.as_view(), name='user-me'),

    url('^.*$', TemplateView.as_view(template_name='index.html'), name='index'),
)
