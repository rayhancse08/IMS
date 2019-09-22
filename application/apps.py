from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'application'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import application.signals
