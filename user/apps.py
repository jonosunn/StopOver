from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    # Register a model signal
    def ready(self):
    	import user.signals
