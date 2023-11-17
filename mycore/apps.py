from django.apps import AppConfig


class MycoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mycore'
   
    def ready(self):
        import mycore.signals  # Import the signals module