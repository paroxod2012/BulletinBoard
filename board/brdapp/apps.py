from django.apps import AppConfig


class BrdappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'brdapp'

    def ready(self):
         import brdapp.signals


