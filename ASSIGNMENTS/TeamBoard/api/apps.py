from django.apps import AppConfig


class ApisConfig(AppConfig):
    name = 'api'

    def ready(self): 
        import api.signals
