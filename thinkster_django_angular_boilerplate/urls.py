from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from rest_framework import routers

from authentication.views import AccountViewSet


router = routers.SimpleRouter()
router.register(r'account', AccountViewSet)


urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),

    url(r'^api/v1/', include(router.urls)),

    url('^.*$', TemplateView.as_view(template_name='index.html'), name='index'),
)
