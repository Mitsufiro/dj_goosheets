from django.apps import AppConfig


class SheetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sheets'
    def ready(self):
        from sheets import updater
        updater.start()