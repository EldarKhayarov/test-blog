from django.apps import AppConfig


class EmailNotifierConfig(AppConfig):
    name = 'email_notifier'

    def ready(self):
        from . import signals
