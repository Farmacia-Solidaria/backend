from django.apps import AppConfig

class DataConfig(AppConfig):
    name = 'modules.data'

    def ready(self) -> None:
        from modules.data import signals