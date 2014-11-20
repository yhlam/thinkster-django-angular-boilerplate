from django.apps import AppConfig


class AuthenticationAppConfig(AppConfig):
    name = 'authentication'
    verbose_name = 'Authentication'

    def ready(self):
        from . import signals
