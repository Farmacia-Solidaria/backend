from django.apps import AppConfig

class DataConfig(AppConfig):
    name = 'modules.data'

    def ready(self) -> None:
        import modules.data.signals