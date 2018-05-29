from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'authentication'

    def ready(self):
        print('TEST!! READY')
        from authentication import signals